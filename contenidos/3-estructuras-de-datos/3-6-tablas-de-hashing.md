---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

# Tablas de _Hash_

Las tablas de _hash_ son estructuras de datos eficientes para almacenar y recuperar información. Emplean una función _hash_ para convertir claves en índices dentro de un arreglo, permitiendo un acceso a los datos en tiempo promedio constante ($O(1)$[^1]). Esto las hace ideales para implementar diccionarios, conjuntos y otras estructuras que demandan búsquedas rápidas. Una tabla de _hash_ extiende la idea de un arreglo tradicional, posibilitando el uso de claves de cualquier tipo para acceder a sus posiciones, gracias a la función _hash_ que asigna cada clave a un índice específico en el arreglo. La eficacia de esta estructura depende de una función _hash_ que sea rápida y distribuya las claves de manera uniforme en el arreglo. La siguiente imagen ilustra los componentes de una tabla de _hash_.

```{figure} ../assets/images/TablaHash1.svg
---
name: tabla_hash
---
Esquema de una tabla de _hash_.
```

Claves
: El universo de claves puede ser muy grande, o infinito. De ese conjunto solo un subconjunto se almacenará en la tabla de _hash_.

Valores
: El valor asociado a una clave. Puede ser cualquier tipo de dato, incluyendo estructuras de datos complejas.

Función de _hash_
: Una función que toma una clave y devuelve un índice en el arreglo.

Arreglo
: La estructura de datos subyacente que almacena los elementos, es un arreglo de pares **`(clave, valor)`{l=go}**. El tamaño del arreglo debe ser lo suficientemente grande para evitar colisiones, pero no tan grande como para desperdiciar espacio. Se debe almacenar el par `(clave, valor)`{l=go} para poder distinguir entre claves diferentes que colisionan en el mismo índice.

Colisiones
: Ocurren cuando dos claves diferentes se mapean al mismo índice en el arreglo. Las colisiones deben manejarse de manera eficiente para garantizar un rendimiento óptimo de la tabla de _hash_.

## Claves

Las claves deben ser **inmutables**, es decir, no pueden modificarse una vez que se han creado. Esto es importante porque la función de _hash_ se basa en el valor de la clave para calcular el índice en el arreglo. Si la clave cambia, el índice también cambiará, lo que puede provocar errores al intentar acceder a los elementos en la tabla de _hash_.

Las claves pueden ser de cualquier tipo de dato, incluyendo enteros, cadenas de texto, estructuras de datos complejas, etc. Es importante que la función de _hash_ sea capaz de manejar todos los tipos de claves que se utilicen, otra opción es utilizar distintas funciones de _hash_ para distintos tipos de claves.

## Colisiones

Un desafío frecuente en las tablas de _hash_ son las colisiones. Estas se producen cuando dos claves distintas son convertidas por la función _hash_ al mismo índice dentro del arreglo. Esto puede deberse a una distribución no uniforme de las claves por la función _hash_ o a una capacidad limitada del arreglo para contener todos los datos. Para resolver este problema, se han desarrollado diversas estrategias, entre las cuales se encuentran:

- _Hashing_ abierto
- _Hashing_ cerrado

## _Hashing_ cerrado con búsqueda lineal

Esta técnica, también conocida como direccionamiento cerrado con sondeo o búsqueda lineal, aborda las colisiones buscando secuencialmente la siguiente ubicación disponible en el arreglo. Cuando una función _hash_ asigna un índice ya ocupado a una nueva clave, en lugar de sobrescribir el elemento existente, se examinan las posiciones subsiguientes del arreglo de forma lineal (incrementando el índice de uno en uno). Este proceso continúa hasta que se encuentra una celda vacía donde se puede almacenar el nuevo elemento. Posteriormente, al buscar un elemento, se aplica la misma función _hash_ a la clave buscada y si la posición inicial está ocupada por un elemento diferente, se sigue la misma secuencia lineal de búsqueda hasta encontrar el elemento deseado o una posición vacía (lo que indicaría que el elemento no está presente).

Si bien esta técnica es fácil de implementar, puede llevar a la formación de _clusters_ o agrupaciones de elementos consecutivos ocupados, lo que puede degradar el rendimiento de las operaciones, ya que se requerirán más comparaciones para encontrar elementos ubicados en estos _clusters_ o posiciones vacías para insertar nuevos elementos. Cuando estos _clusters_ crecen demasiado se degrada el rendimiento de la tabla. Para mitigar este problema se pueden utilizar diferentes técnicas como el sondeo cuadrático que en lugar de incrementar el índice de uno en uno, lo hace de acuerdo a una función cuadrática predeterminada o el doble _hashing_ que utiliza una segunda función de _hash_ para determinar el incremento del índice.

Esta técnica requiere poder distinguir entre posiciones vacías en la tabla y posiciones donde se han borrado elementos. Para ello se debe marcar las posiciones eliminadas con algún marcador especial. Esto permite que la búsqueda continúe sin problemas.

### Inserción

En la siguiente figura se grafica la inserción de un elemento en una tabla de _hash_ cerrada.

```{figure} ../assets/images/TablaHashInsercion.svg
---
name: tabla_hash_insercion_cerrada
---
Inserción en una tabla de _hash_ cerrada.
```

Supongamos que vamos a insertar las claves $k_1$ y $k_2$, en ese orden, y que la posición 10 del arreglo ya se encontraba ocupada. En este caso, $f(k_1)$ devuelve el índice 9, como inicialmente la posición se encuentra vacía, se puede asociar la clave a ese índice. Luego $f(k_2)$ también devuelve 9, como la posición 9 se encuentra ocupada, intenta en la próxima, como la posición 10 ya está ocupada incrementa en forma circular el índice y finalmente puede asociar $k_2$ a la posición 0 del arreglo.

### Eliminación

La eliminación de un elemento en una tabla de _hash_ cerrada es un poco más complicada que la inserción. Cuando se elimina un elemento, se debe marcar la posición como eliminada, pero no se puede dejar la posición vacía, ya que esto podría causar problemas al buscar otros elementos en el futuro. En su lugar, se debe utilizar un marcador especial para indicar que la posición ha sido eliminada.

Esto se conoce como _marcador de eliminación_ y permite que la búsqueda continúe sin problemas. Sin embargo, esto puede aumentar el tiempo de búsqueda si hay muchos elementos eliminados en la tabla de _hash_.

```{figure} ../assets/images/TablaHashEliminacion.svg
---
name: tabla_hash_eliminacion_cerrada
---
Eliminación en una tabla de _hash_ cerrada.
```

En la figura se observa que al eliminar el elemento en la posición 10, se marca la posición como eliminada, pero no se deja vacía. Esto permite que la búsqueda de otros elementos continúe sin problemas. En resumen una posición de la tabla podrá estar en algunos de los tres siguientes estados:

- Vacía
- Ocupada
- Eliminada

### Búsqueda

La búsqueda de un elemento en una tabla de _hash_ cerrada es similar a la inserción. Se utiliza la función de _hash_ para calcular el índice y luego se busca el elemento en esa posición. Si el elemento no se encuentra en la posición calculada, se incrementa el índice en 1 hasta encontrar el elemento o una posición vacía. Si se encuentra una posición eliminada, la búsqueda continua.

```{figure} ../assets/images/TablaHashBusquedaCerrada.svg
---
name: tabla_hash_busqueda_cerrada
---
Búsqueda en una tabla de _hash_ cerrada.
```

En la figura se observa que al buscar la clave $k_2$, se intenta con la posición 9, como la clave asociada a esa posición es $k_1$, la búsqueda continua, luego la posición 10 está eliminada, por lo que se avanza a la posición 0 donde finalmente se encuentra la clave buscada.

Supongamos que se busca una clave $k_3$ cuyo valor de _hash_ también es 9. En este caso, la búsqueda comenzaría en la posición 9, pero como la clave asociada a esa posición es $k_1$, la búsqueda continuaría hasta encontrar la clave o una posición vacía. En este caso en la posición 1 se encuentra con una posición vacía, por lo que se concluye que la clave $k_3$ no está presente en la tabla de _hash_.

### Aritmética Modular

Es la aritmética que deriva del estudio del resto de la división de enteros. Es una forma de realizar cálculos en un conjunto finito de números. En el caso del _hashing_ cerrado, se utiliza para calcular el índice en el arreglo. La operación más común en la aritmética modular es el operador módulo, que devuelve el resto de la división de dos números.

La operación de módulo se denota como $a \bmod b$, donde $a$ es el número que se va a dividir y $b$ es el divisor. El resultado de la operación es el resto de la división de $a$ entre $b$. Por ejemplo, $7 \bmod 3 = 1$, ya que al dividir 7 entre 3, el cociente es 2 y el resto es 1.

Algunas propiedades de la aritmética modular son:

- $a \bmod n + b \bmod n = (a + b) \bmod n$
- $a \bmod n - b \bmod n = (a - b) \bmod n$
- $(a \bmod n) * (b \bmod n) = (a * b) \bmod n$
- $(a \bmod n) \div (b \bmod n) = (a \div b) \bmod n$ (si $b \neq 0$)

## _Hashing_ abierto

El _hashing_ abierto, es una técnica fundamental para el manejo de colisiones en tablas de _hash_. En contraste con el direccionamiento cerrado, donde todos los elementos se almacenan directamente dentro del arreglo subyacente, el _hashing_ abierto utiliza una estructura de datos adicional (generalmente una lista enlazada). En cada posición del arreglo se encuentra una lista enlazada para almacenar los elementos que colisionan en ese índice. Cuando dos o más claves diferentes se "mapean" a la misma posición en la tabla, en lugar de buscar otra posición en el arreglo, simplemente se añaden los nuevos elementos a la lista existente en esa posición. Esto significa que múltiples elementos pueden residir en la misma posición del arreglo, encadenados en una lista.

```{figure} ../assets/images/TablaHashAbierta.svg
---
name: tabla_hash_abierta
---
Tabla de _hash_ abierta.
```

## Consideraciones de diseño

Al diseñar una tabla de _hash_ es muy importante evitar colisiones y al mismo tiempo ocupar el menor espacio posible. Para ello se deben considerar los siguientes aspectos:

### Factor de carga

El factor de carga ($\alpha$) es una métrica crucial para evaluar y predecir el rendimiento de una tabla de _hash_. Se define formalmente como la relación entre el número de elementos ($n$) actualmente almacenados en la tabla y el tamaño ($m$) del arreglo subyacente:

$$
\alpha = \frac{n}{m}
$$

Este valor proporciona una indicación de cuán "llena" está la tabla de _hash_. La intuición detrás del factor de carga es que a medida que la tabla se llena (es decir, a medida que $\alpha$ se acerca o supera a 1), la probabilidad de que nuevas claves colisionen con posiciones ya ocupadas aumenta significativamente.

Se recomienda mantener el factor de carga por debajo de 0.75 como una guía general basada en el compromiso entre el rendimiento y la utilización del espacio. Este umbral suele ser un buen punto de equilibrio para muchas aplicaciones que utilizan técnicas de _hashing_ cerrado. Sin embargo, el factor de carga óptimo puede variar dependiendo de:

La técnica de resolución de colisiones utilizada
: El _hashing_ abierto puede tolerar factores de carga más altos (incluso mayores que 1) antes de que el rendimiento se degrade significativamente en comparación con el direccionamiento cerrado. En el _hashing_ abierto, un factor de carga $\alpha$ significa que en promedio, cada lista tendrá $\alpha$ elementos.

Los requisitos específicos de la aplicación
: Si la eficiencia de las operaciones es primordial, se podría optar por un factor de carga más bajo. Si el espacio es una limitación crítica, se podría tolerar un factor de carga más alto a expensas de un posible impacto en el rendimiento.

La calidad de la función hash
: Una función hash que distribuye las claves de manera más uniforme permitirá un rendimiento aceptable incluso con factores de carga ligeramente más altos, ya que habrá menos colisiones para el mismo número de elementos.

### Tamaño del arreglo

Se recomienda que el tamaño del arreglo ($m$) en una tabla de _hash_ sea un **número primo**. Esto se fundamenta en principios matemáticos relacionados con la distribución uniforme de las claves al aplicar la función _hash_ y la aritmética modular. Si bien no es una regla absoluta y existen implementaciones exitosas con tamaños no primos, utilizar un tamaño de arreglo primo puede mitigar ciertos patrones de colisión y mejorar la dispersión de las claves, especialmente cuando se combinan con ciertas funciones _hash_.

Si la posición de una clave en el arreglo se calcula como:

$$
\textit{indice} = \text{hash}(\textit{clave}) \bmod m
$$

Si $m$ es un número primo, la función $\text{hash}$ tiende a distribuir las claves de manera más uniforme en el arreglo. Esto se debe a que los números primos no tienen divisores comunes con otros números, lo que reduce la probabilidad de que diferentes claves generen el mismo índice.

Otras tablas de _hash_ que no utilizan la aritmética modular, no necesitan que el tamaño del arreglo sea primo. En estos casos, el tamaño del arreglo puede ser cualquier número entero positivo.

### Funciones de _hash_

La función de _hash_ es el corazón de cualquier tabla de _hash_. Su propósito fundamental es tomar una clave de entrada (que puede ser de cualquier tipo de dato: números, cadenas de texto, objetos complejos, etc.) y transformarla en un índice entero dentro del rango válido del arreglo subyacente de la tabla de _hash_ (típicamente de 0 a $m$−1, donde $m$ es el tamaño del arreglo).

Las dos características primordiales que una buena función de _hash_ debe poseer son la eficiencia y la distribución uniforme:

Eficiencia
: Es crucial que su cálculo sea rápido y se pueda realizar en $O(1)$ con respecto al tamaño de la clave. Las funciones de _hash_ se construyen utilizando operaciones aritméticas y lógicas básicas que son inherentemente rápidas a nivel de hardware como sumas, restas, multiplicaciones, divisiones enteras, módulos y operaciones bit a bit como `AND`, `OR`, `XOR`, y desplazamientos de bits.

Distribución Uniforme
: El objetivo ideal de una función de _hash_ es asignar cada clave posible a un índice único dentro del arreglo. Sin embargo, dado que el espacio de posibles claves suele ser mucho mayor que el tamaño del arreglo, las colisiones son inevitables. Una buena función de _hash_ minimiza la probabilidad de colisiones al distribuir las claves de entrada de la manera más uniforme posible a lo largo de los índices del arreglo. Esto significa que para un conjunto de claves dado, la función $\text{hash}$ debería intentar dispersarlas equitativamente entre las m posiciones del arreglo, evitando la concentración de muchas claves en unas pocas posiciones.

Por ejemplo para cadenas de caracteres se puede usar la **Multiplicación Polinómica** que trata la cadena como un polinomio donde los caracteres son los coeficientes de un polinomio. (Más efectivo para evitar colisiones con anagramas).

Sea la cadena $S = c_1 c_2 \dots c_n$ donde $c_i$ es el $i$-ésimo carácter de la cadena. Cada caracter se puede "mapear" un valor numérico utilizando su código ASCII. Sea $a$ una constante elegida (a menudo un número primo) y $m$ el tamaño del arreglo de la tabla de _hash_ (generalmente un número primo). La función de _hash_ se puede definir como:

$$
h(S) = (c_1 \cdot a^{n-1} + c_2 \cdot a^{n-2} + \dots + c_n \cdot a^0) \bmod m
$$

El módulo se aplica al resultado final para asegurar que el valor hash esté dentro del rango válido de índices del arreglo $[0, m−1]$.

## Ejemplo de implementación de _hashing_ cerrado

```{code-block} go
// hashtable proporciona una implementación de una tabla hash cerrada cuyas
// claves son cadenas de caracteres y los valores pueden ser de cualquier tipo.
// La tabla utiliza un arreglo para almacenar pares clave-valor.
package hashtable

import (
    "fmt"
    "math"
)

// hashTableEntry representa una entrada en la tabla hash, que contiene una
// clave y su valor asociado.
type hashTableEntry[K string, V any] struct {
    key   K
    value V
}

// HashTable es una tabla hash cerrada que utiliza un arreglo para almacenar
// elementos. La tabla solo soporta string como claves y cualquier tipo como
// valores. En cada posición del arreglo se almacena un par clave-valor.
type HashTable[K string, V any] struct {
    // arreglo de entradas de la tabla hash.
    buckets []*hashTableEntry[K, V]
    // size es el número de elementos en la tabla.
    size uint
    // capacity es la capacidad de la tabla.
    capacity uint
    // loadFactor es el factor de carga de la tabla.
    loadFactor float32
    // threshold es el umbral de carga para redimensionar la tabla.
    threshold uint
}

// NewHashTable crea una nueva tabla de hash cerrada con la capacidad y el
// factor de carga especificados.
//
// - Si la capacidad es igual a 0, se establece en 17.
//
// - Si el factor de carga es menor o igual a 0 o mayor que 1, se establece en
// 0.75.
//
// - Si la capacidad no es un número primo, se redimensiona a la siguiente
// capacidad primo mayor o igual a la capacidad especificada.
func NewHashTable[K string, V any](capacity uint, loadFactor float32) *HashTable[K, V] {
    if capacity == 0 {
        capacity = 17
    }
    if loadFactor <= 0 || loadFactor > 1 {
        loadFactor = 0.75
    }
    if !isPrime(capacity) {
        capacity = nextPrime(capacity)
    }
    return &HashTable[K, V]{
        buckets:    make([]*hashTableEntry[K, V], capacity),
        size:       0,
        capacity:   capacity,
        loadFactor: loadFactor,
        threshold:  uint(float32(capacity) * loadFactor),
    }
}

// Put agrega un nuevo par clave-valor a la tabla de hash. Si la clave ya
// existe, actualiza el valor asociado a la clave.
//
// Devuelve true si se agregó o actualizó el elemento, false si la clave es nula.
//
// - Si la tabla de hash está llena, se redimensiona automáticamente.
//
// - Si la clave es nula, no se agrega nada.
func (ht *HashTable[K, V]) Put(key K, value V) {
    // Si la clave ya existe, actualizamos el valor.
    if index, esta := ht.getIndex(key); esta {
        ht.buckets[index].value = value
        return
    }

    // Si la clave es nula, no se agrega nada.
    if key == "" {
        return
    }

    // Si la tabla de hash está llena, redimensionamos.
    if ht.size >= ht.threshold {
        ht.resize()
    }

    // La clave no existe, así que la agregamos.
    index := ht.hash(key) % ht.capacity
    for {
        if ht.buckets[index] == nil || ht.buckets[index].key == "" {
            // Si el bucket está vacío, insertamos el nuevo par clave-valor.
            ht.buckets[index] = &hashTableEntry[K, V]{key: key, value: value}
            ht.size++
            return
        }
        // Si el bucket está ocupado probamos el siguiente índice.
        index = (index + 1) % ht.capacity
    }
}


// Get devuelve el valor asociado a la clave dada y true para indicar que
// encontró la clave buscada.
//
// - Si la clave no existe o es nula, devuelve false y un valor nulo.
func (ht *HashTable[K, V]) Get(key K) (V, bool) {
    index, exists := ht.getIndex(key)
    if !exists {
        var zeroValue V
        return zeroValue, exists
    }
    return ht.buckets[index].value, exists
}

// Remove elimina el par clave-valor asociado a la clave dada.
//
// Devuelve true si se eliminó el elemento, false si la clave no existe.
func (ht *HashTable[K, V]) Remove(key K) bool {
    index, exists := ht.getIndex(key)
    if exists {
        var zeroValue V
        ht.buckets[index].key = "" //marca la clave como nula para indicar que fue eliminada
        ht.buckets[index].value = zeroValue
        ht.size--
    }
    return exists
}

// Keys devuelve una lista de todas las claves en la tabla de hash.
func (ht *HashTable[K, V]) Keys() []K {
    keys := make([]K, 0, ht.size)
    for _, node := range ht.buckets {
        if node != nil && node.key != "" {
            keys = append(keys, node.key)
        }
    }
    return keys
}

// Values devuelve una lista de todos los valores en la tabla de hash.
func (ht *HashTable[K, V]) Values() []V {
    values := make([]V, 0, ht.size)
    for _, node := range ht.buckets {
        if node != nil && node.key != "" {
            values = append(values, node.value)
        }
    }
    return values
}

// Size devuelve el número de elementos en la tabla de hash.
func (ht *HashTable[K, V]) Size() uint {
    return ht.size
}

// IsEmpty devuelve true si la tabla de hash está vacía, false en caso contrario.
func (ht *HashTable[K, V]) IsEmpty() bool {
    return ht.size == 0
}

// Clear elimina todos los elementos de la tabla de hash.
func (ht *HashTable[K, V]) Clear() {
    ht.buckets = make([]*hashTableEntry[K, V], ht.capacity)
    ht.size = 0
}

// String devuelve una representación en cadena de la tabla de hash.
func (ht *HashTable[K, V]) String() string {
    result := "{"
    for _, node := range ht.buckets {
        if node != nil && node.key != "" {
            result += fmt.Sprintf("%v: %v", node.key, node.value) + ", "
        }
    }
    if len(result) > 1 {
        result = result[:len(result)-2]
    }
    result += "}"
    return result
}

// Funciones privadas //////////////////////////////////////////////////////////

// a es una constante utilizada para calcular el hash de un string
const a float64 = 11.0

// hash calcula el índice del bucket para una clave dada.
//
// Se utiliza la técnica de Mulitiplicación Polinómica.
func (ht *HashTable[K, V]) hash(key K) uint {
    l := len(key)
    var hash uint = 0
    for i, c := range key {
        hash += uint(c) * uint(math.Pow(a, float64(l-i-1)))
    }
    return hash
}

// getIndex devuelve el índice del bucket para una clave dada y un booleano que
// indica si la clave existe.
func (ht *HashTable[K, V]) getIndex(key K) (uint, bool) {
    if key == "" {
        return 0, false
    }
    for index := ht.hash(key) % ht.capacity; ht.buckets[index] != nil; index = (index + 1) % ht.capacity {
        if ht.buckets[index].key == key {
            return index, true
        }
    }
    return 0, false
}

// resize redimensiona la tabla de hash y reubica todos los elementos en la
// nueva tabla.
//
// El nuevo tamaño es el siguiente número primo mayor o igual al doble de la
// capacidad actual.
func (ht *HashTable[K, V]) resize() {
    newCapacity := nextPrime(ht.capacity * 2)
    newBuckets := make([]*hashTableEntry[K, V], newCapacity)

    // Reinsertar todos los elementos en el nuevo arreglo, manejando colisiones
    for _, node := range ht.buckets {
        if node != nil && node.key != "" {
            index := ht.hash(node.key) % newCapacity
            for newBuckets[index] != nil {
                // Resolver colisiones con prueba lineal
                index = (index + 1) % newCapacity
            }
            newBuckets[index] = node
        }
    }

    // Actualizar los atributos de la tabla hash
    ht.buckets = newBuckets
    ht.capacity = newCapacity
    ht.threshold = uint(float32(newCapacity) * ht.loadFactor)
}

// nextPrime devuelve el siguiente número primo mayor o igual a n.
func nextPrime(n uint) uint {
    if n <= 1 {
        return 2
    }
    for i := n; ; i++ {
        if isPrime(i) {
            return i
        }
    }
}

// isPrime devuelve true si n es un número primo, false en caso contrario.
func isPrime(n uint) bool {
    if n <= 1 {
        return false
    }
    if n <= 3 {
        return true
    }
    if n%2 == 0 || n%3 == 0 {
        return false
    }
    for i := uint(5); i*i <= n; i += 6 {
        if n%i == 0 || n%(i+2) == 0 {
            return false
        }
    }
    return true
}
```

En el ejemplo sólo se implementa para claves del tipo cadena de caracteres y valores de cualquier tipo.

Para otros tipos de claves se debe implementar una función de _hash_ diferente.

Para implementar una tabla de _hash_ genérica, que soporte cualquier tipo de claves y valores, se puede utilizar la función de _hash_ de Go. Sin embargo, esto puede ser menos eficiente que utilizar una función de _hash_ específica para el tipo de clave que se está utilizando.

## Ejercicios

1. Modificar la tabla de _hash_ cerrada para que las claves puedan ser de distintos tipos (usar el paquete [`maphash`](https://pkg.go.dev/hash/maphash) de Go).

2. Implementar una tabla de _hash_ abierta. Para ello se debe implementar una lista enlazada que almacene los elementos en cada posición del arreglo. Cuando se produce una colisión, el nuevo elemento se agrega a la lista en la posición correspondiente. La tabla debe tener los mismos métodos que la tabla de _hash_ cerrada: `Put`{l=go}, `Get`{l=go}, `Remove`{l=go}, `Keys`{l=go}, `Values`{l=go}, `Size`{l=go}, `IsEmpty`{l=go}, `Clear`{l=go} y `String`{l=go}. Las claves deben ser de cualquier tipo.

3. Escribir casos de pruebas que cubran todas las operaciones de los puntos anteriores.

[^1]: En este caso se toma el tiempo promedio, bajo ciertas condiciones. Cuando se evalua un TAD donde se insertan, buscan y remueven elementos muy frecuentemente, se acostumbra tomar el tiempo promedio de las operaciones. Sin embargo, en el peor de los casos, algunas operaciones pueden tener un orden lineal.
