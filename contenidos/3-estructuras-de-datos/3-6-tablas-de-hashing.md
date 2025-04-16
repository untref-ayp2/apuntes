---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Tablas de _Hashing_

Las tablas de _hashing_ son estructuras de datos que permiten almacenar y recuperar información de manera eficiente. Utilizan una función de _hash_ para mapear claves a posiciones en un arreglo, lo que permite acceder a los elementos en tiempo constante $O(1)$[^1]. Son especialmente útiles para implementar diccionarios, conjuntos y otras estructuras de datos que requieren acceso rápido a los elementos.

[^1]: En este caso se toma el tiempo promedio, bajo ciertas condiciones. Cuando se evalua un TAD donde se insertan, buscan y remueven elementos muy frecuentemente, se acostumbra tomar el tiempo promedio de las operaciones. Sin embargo, en el peor de los casos, algunas operaciones pueden tener un orden lineal.

Una tabla de _hashing_ generaliza el concepto de arreglo, ya que permite acceder a cualquier posición de la tabla en tiempo constante. Podemos asi tener arreglos indexados con otros tipos de datos y no solo enteros. 

Para lograr esto, se utiliza una función de _hash_ que toma una clave y devuelve un índice en el arreglo. La función de _hash_ debe ser eficiente y distribuir el conjunto de claves uniformemente dentro del arreglo.

En la siguiente figura se aprecia un esquema que nos permite analizar los distintos elementos involucrados en una tabla de _hashing_. 


```{figure} ../assets/images/TablaHash1.svg
---
name: tabla_hash
---
Esquema de una tabla de _hashing_.
```

Claves
: El universo de claves puede ser muy grande, o infinito. De ese conjunto solo un subconjunto se almacenará en la tabla de _hashing_. 

Valores
: El valor asociado a una clave. Puede ser cualquier tipo de dato, incluyendo estructuras de datos complejas.

Función de _hash_
: Una función que toma una clave y devuelve un índice en el arreglo.

Arreglo
: La estructura de datos subyacente que almacena los elementos, es un arreglo de _"valores"_. El tamaño del arreglo debe ser lo suficientemente grande para evitar colisiones, pero no tan grande como para desperdiciar espacio.

Colisiones
: Ocurren cuando dos claves diferentes se mapean al mismo índice en el arreglo. Las colisiones deben manejarse de manera eficiente para garantizar un rendimiento óptimo de la tabla de _hashing_.

## Claves

Las claves deben ser inmutables, es decir, no deben cambiar una vez que se han creado. Esto es importante porque la función de _hash_ se basa en el valor de la clave para calcular el índice en el arreglo. Si la clave cambia, el índice también cambiará, lo que puede provocar errores al intentar acceder a los elementos en la tabla de _hashing_.
Las claves pueden ser de cualquier tipo de dato, incluyendo enteros, cadenas de texto, estructuras de datos complejas, etc. Sin embargo, es importante que la función de _hash_ sea capaz de manejar todos los tipos de claves que se utilicen en la tabla de _hashing_.

## Colisiones

Las colisiones son un problema común en las tablas de _hashing_. Ocurren cuando dos claves diferentes se mapean al mismo índice en el arreglo. Esto puede suceder si la función de _hash_ no distribuye uniformemente las claves en el arreglo o si el tamaño del arreglo es demasiado pequeño.
Para manejar las colisiones, existen varias técnicas, entre las que se encuentran:

_Hashing_ abierto
: Con esta técnica, cuando se produce una colisión, se busca la siguiente posición libre en el arreglo para almacenar el nuevo elemento, simplemente incrementando el índice hasta encontrar una posición libre[^2].

[^2]: Otras versiones de esta técnica utilizan una función de _hash_ diferente para encontrar la siguiente posición libre, lo que se conoce como _hashing_ doble.

_Hashing_ cerrado
: Con esta técnica, el arreglo subyacente contiene una lista de elementos en cada posición. Cuando se produce una colisión, el nuevo elemento se agrega a la lista en la posición correspondiente. Esta técnica es más eficiente en términos de espacio, pero puede ser más lenta en términos de tiempo de acceso.

## _Hashing_ abierto

Cuando se produce una colisión se debe incrementar el índice en 1 hasta encontrar una posición libre. Esta técnica es simple de implementar y funciona bien en la mayoría de los casos. Sin embargo, puede ser ineficiente si hay muchas colisiones, ya que puede requerir un tiempo de búsqueda lineal en el peor de los casos. Es importante elegir una función de _hash_ que minimice las colisiones y un tamaño de arreglo que sea lo suficientemente grande para evitar colisiones.

Cuando se incrementa el índice, se debe tener en cuenta el tamaño del arreglo. Si el índice supera el tamaño del arreglo, se debe volver al principio del arreglo y continuar buscando una posición libre. Esto se conoce como _hashing_ circular.

### Inserción

En la siguiente figura se grafica la inserción de un elemento en una tabla de _hashing_ abierta.

```{figure} ../assets/images/TablaHashInsercion.svg
---
name: tabla_hash_insercion_abierta
---
Inserción en una tabla de _hash_ abierta.
```

Supongamos que vamos a insertar las claves $k_1$ y $k_2$, en ese orden, y que la posición 10 del arreglo ya se encontraba ocupada. En este caso, $f(k_1)$ devuelve el índice 9, como inicialmente la posición se encuentra vacía, se puede asociar la clave a ese índice. Luego $f(k_2)$ también devuelve 9, como la posición 9 se encuentra ocupada, intenta en la próxima, como la posición 10 ya está ocupada incrementa en forma circular el índice y finalmente puede asociar $k_2$ a la posición 0 del arreglo.

### Eliminación

La eliminación de un elemento en una tabla de _hashing_ abierta es un poco más complicada que la inserción. Cuando se elimina un elemento, se debe marcar la posición como eliminada, pero no se puede dejar la posición vacía, ya que esto podría causar problemas al buscar otros elementos en el futuro. En su lugar, se debe utilizar un marcador especial para indicar que la posición ha sido eliminada.
Esto se conoce como _marcador de eliminación_ y permite que la búsqueda continúe sin problemas. Sin embargo, esto puede aumentar el tiempo de búsqueda si hay muchos elementos eliminados en la tabla de _hashing_.

```{figure} ../assets/images/TablaHashEliminacion.svg
---
name: tabla_hash_eliminacion_abierta
---
Eliminación en una tabla de _hash_ abierta.
```
En la figura se observa que al eliminar el elemento en la posición 10, se marca la posición como eliminada, pero no se deja vacía. Esto permite que la búsqueda de otros elementos continúe sin problemas. Sin embargo, si hay muchos elementos eliminados en la tabla de _hashing_, esto puede aumentar el tiempo de búsqueda. En resumen una posición de la tabla podrá estar en algunos de los tres siguientes estados:
- Vacía
- Ocupada
- Eliminada

### Búsqueda

La búsqueda de un elemento en una tabla de _hashing_ abierta es similar a la inserción. Se utiliza la función de _hash_ para calcular el índice y luego se busca el elemento en esa posición. Si el elemento no se encuentra en la posición calculada, se incrementa el índice en 1 hasta encontrar el elemento o una posición vacía. Si se encuentra una posición eliminada, la búsqueda continua.

```{figure} ../assets/images/TablaHashBusquedaAbierta.svg
---
name: tabla_hash_busqueda_abierta
---
Búsqueda en una tabla de _hash_ abierta.
```
En la figura se observa que al buscar la clave $k_2$, se intenta con la posición 9, como la clave asociada a esa posición es $k_1$, la búsqueda continua, luego la posición 10 está eliminada, por lo que se avanza a la posición 0 donde finalmente se encuentra la clave buscada.

Supongamos que se busca una clave $k_3$ cuyo valor de _hash_ también es 9. En este caso, la búsqueda comenzaría en la posición 9, pero como la clave asociada a esa posición es $k_1$, la búsqueda continuaría hasta encontrar una posición vacía o eliminada. En este caso en la posición 1 se encuentra con una posición vacía, por lo que se concluye que la clave $k_3$ no está presente en la tabla de _hashing_.

## _Hashing_ cerrado

El _hashing_ cerrado es una técnica de manejo de colisiones que utiliza listas enlazadas para almacenar los elementos en cada posición del arreglo. Cuando se produce una colisión, el nuevo elemento se agrega a la lista en la posición correspondiente. Esta técnica es más eficiente en términos de espacio, ya que no requiere un tamaño fijo para el arreglo, pero puede ser más lenta en términos de tiempo de acceso.

```{figure} ../assets/images/TablaHashCerrado.svg
---
name: tabla_hash_cerrado
---
Tabla de _hashing_ cerrada.
```

## Aritmética Modular

Es la aritmética que deriva del estudio del resto de la división de enteros. Es una forma de realizar cálculos en un conjunto finito de números. En el caso de las tablas de _hashing_, se utiliza para calcular el índice en el arreglo a partir de la clave. La operación más común en la aritmética modular es el operador módulo, que devuelve el resto de la división de dos números.

La operación de módulo se denota como $a \mod b$, donde $a$ es el número que se va a dividir y $b$ es el divisor. El resultado de la operación es el resto de la división de $a$ entre $b$. Por ejemplo, $7 \mod 3 = 1$, ya que al dividir 7 entre 3, el cociente es 2 y el resto es 1.

Algunas propiedades de la aritmética modular son:
- $a \mod n + b \mod n = (a + b) \mod n$
- $a \mod n - b \mod n = (a - b) \mod n$
- $a \mod n * b \mod n = (a * b) \mod n$
- $a \mod n / b \mod n = (a / b) \mod n$ (si $b \neq 0$)

## Consideraciones de diseño

Al diseñar una tabla de _hashing_ es muy importante evitar colisiones y al mismo tiempo ocupar el menor espacio posible. Para ello se deben considerar los siguientes aspectos:

Factor de carga
: El factor de carga es la relación entre el número de elementos en la tabla y el tamaño del arreglo. Un factor de carga alto puede aumentar el número de colisiones y disminuir el rendimiento de la tabla de _hashing_. Por lo general, se recomienda mantener el factor de carga por debajo de 0.75 para garantizar un rendimiento óptimo. Por lo contrario, un factor de carga bajo implica disminuir las colisiones al costo de aumentar el espacio utilizado.

Tamaño del arreglo
: El tamaño del arreglo debería ser un número primo. Esto se debe a que los números primos tienen propiedades matemáticas que ayudan a distribuir uniformemente las claves en el arreglo cuando se utiliza aritmética modular.

Funciones de _hash_
: La función de _hash_ debe ser eficiente y distribuir uniformemente las claves en el arreglo. Las funciones de _hash_ se basan en operaciones simples como sumas, restas, productos, división y potencia de números que se pueden realizar en tiempo constante. Generalmente como la función de _hash_ puede generar un índice por fuera del arreglo subyacente por lo que se utiliza aritmética modular.

## Ejemplo de implementación de _hashing_ abierto

```{code-block} go
// Paquete hashtable proporciona una implementación de una tabla hash abierta
// cuyas claves son cadenas de caracteres y los valores pueden ser
// de cualquier tipo. La tabla utiliza un arreglo para almacenar
// pares clave-valor.
//
// hashTableEntry representa un único nodo en la tabla hash, que contiene una clave
// y su valor asociado.
//
// HashTable es una tabla hash abierta que utiliza un arreglo para almacenar elementos.
// La tabla solo soporta string como claves y cualquier tipo como valores.

package hashtable

import (
	"fmt"
	"math"
)

// hashTableEntry representa una entrada en la tabla hash, que contiene una clave y su valor asociado.
type hashTableEntry[K string, V any] struct {
	key   K
	value V
}

// HashTable es una tabla de hash abierta. En cada posición
// del arreglo se almacena un par clave-valor.
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

// NewHashTable crea una nueva tabla de hash abierta con la capacidad y el factor de carga especificados.
// Si la capacidad es igual a 0, se establece en 17.
// Si el factor de carga es menor o igual a 0 o mayor que 1, se establece en 0.75.
// Si la capacidad no es un número primo, se redimensiona a la siguiente capacidad
// primo mayor o igual a la capacidad especificada.
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

// hash calcula el índice del bucket para una clave dada.
// Se calcula como el valor ASCII de cada caracter de la clave, elevado a
// la potencia de su posición + 1
func (ht *HashTable[K, V]) hash(key K) uint {
	var hash uint = 0
	for i, c := range key {
		hash += uint(math.Pow(float64(c), float64(i+1)))
	}

	return hash
}

// Put agrega un nuevo par clave-valor a la tabla de hash. Si la clave ya existe,
// actualiza el valor asociado a la clave.
// Devuelve true si se agregó o actualizó el elemento, false si la clave es nula.
// Si la tabla de hash está llena, se redimensiona automáticamente.
// Si la clave es nula, no se agrega nada.

func (ht *HashTable[K, V]) Put(key K, value V) {
	// Si la clave es nula, no se agrega nada.
	if key == "" {
		return
	}
	// Si la tabla de hash está llena, redimensionamos.
    if ht.size >= ht.threshold {
        ht.resize()
    }

    index := ht.hash(key) % ht.capacity
    for {
        if ht.buckets[index] == nil {
            // Si el bucket está vacío, insertamos el nuevo par clave-valor.
            ht.buckets[index] = &hashTableEntry[K, V]{key: key, value: value}
            ht.size++
            return
        } else if ht.buckets[index].key == key {
            // Si la clave ya existe, actualizamos el valor.
            ht.buckets[index].value = value
            return
        }
        // Si el bucket está ocupado y la clave no coincide, probamos el siguiente índice.
        index = (index + 1) % ht.capacity
    }
}
// Get devuelve el valor asociado a la clave dada y true para indicar que encontró
// la clave buscada.
// Si la clave no existe o es nula, devuelve false y un valor nulo.

func (ht *HashTable[K, V]) Get(key K) (V, bool) {
	var zeroValue V
	
	index, esta := ht.getIndex(key)
	if esta {
		return ht.buckets[index].value, esta
	}
	return zeroValue, esta
}

// getIndex devuelve el índice del bucket para una clave dada.
// y un booleano que indica si la clave existe.
func (ht *HashTable[K, V]) getIndex(key K) (uint, bool) {
	if key == "" {
		return 0, false
	}
	for index := ht.hash(key) % ht.capacity; ht.buckets[index] != nil; index=(index+1)%ht.capacity {
		if ht.buckets[index].key == key {
			return index, true
		}
	}
	return 0, false
}

// Remove elimina el par clave-valor asociado a la clave dada. Devuelve true si se eliminó
// el elemento, false si la clave no existe.
func (ht *HashTable[K, V]) Remove(key K) bool {
	var zeroValue V
	index, esta := ht.getIndex(key)
	if esta {
		ht.buckets[index].key = "" //marca la clave como nula para indicar que fue eliminada
		ht.buckets[index].value = zeroValue
	}
	return esta
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

func (ht *HashTable[K, V]) resize() {
    newCapacity := ht.capacity * 2
    newCapacity = nextPrime(newCapacity)
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
```

En el ejemplo sólo se implementa para claves del tipo cadena de caracteres y valores de cualquier tipo. La función de _hash_ se basa en el valor ASCII de cada carácter de la clave, elevado a la potencia de su posición + 1. Esto permite distribuir uniformemente las claves en el arreglo y minimizar las colisiones.

Para otros tipos de claves se debe implementar una función de hash diferente. 

Una tabla de _hashing_ genérica, que soporte cualquier tipo de claves y valores, puede ser implementada utilizando la función de _hash_ de Go. Sin embargo, esto puede ser menos eficiente que utilizar una función de _hash_ específica para el tipo de clave que se está utilizando.

## Ejercicios

1- Modificar la tabla de _hashing_ abierto para que las claves puedan ser de distintos tipos (usar el paquete [`maphash`](https://pkg.go.dev/hash/maphash) de Go).

2- Implementar una tabla de _hashing_ cerrada. Para ello se debe implementar una lista enlazada que almacene los elementos en cada posición del arreglo. Cuando se produce una colisión, el nuevo elemento se agrega a la lista en la posición correspondiente. La tabla debe tener los mismos métodos que la tabla de _hashing_ abierta: `Put`, `Get`, `Remove`, `Keys`, `Values`, `Size`, `IsEmpty`, `Clear` y `String`. Las claves deben ser de cualquier tipo.

3- Escribir casos de pruebas que cubran todas las operaciones de los puntos anteriores.