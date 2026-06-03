package hashtable

import (
	"errors"
	"fmt"
)

// hashTableEntry representa una entrada en la tabla hash, que contiene una
// clave, su valor asociado y un marcador de eliminación.
//
// El campo deleted (tombstone) evita perder la posición al eliminar: en lugar
// de compactar el arreglo, se marca la entrada como eliminada para que las
// búsquedas lineales no se interrumpan.
type hashTableEntry[K comparable, V any] struct {
	key     K
	value   V
	deleted bool
}

// HashTableOpenAddressing es una implementación de hashing cerrado con sondeo
// lineal que utiliza un arreglo para almacenar pares clave-valor.
type HashTableOpenAddressing[K comparable, V any] struct {
	// arreglo de entradas de la tabla hash.
	buckets []*hashTableEntry[K, V]
	// size es el número de elementos en la tabla.
	size int
	// capacity es la capacidad de la tabla.
	capacity int
	// loadFactor es el factor de carga de la tabla.
	loadFactor float32
	// threshold es el umbral de carga para redimensionar la tabla.
	threshold int
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
func NewHashTableOpenAddressing[K comparable, V any](capacity int, loadFactor float32) *HashTableOpenAddressing[K, V] {
	if capacity == 0 {
		capacity = 17
	}
	if loadFactor <= 0 || loadFactor > 1 {
		loadFactor = 0.75
	}
	if !isPrime(capacity) {
		capacity = nextPrime(capacity)
	}
	return &HashTableOpenAddressing[K, V]{
		buckets:    make([]*hashTableEntry[K, V], capacity),
		size:       0,
		capacity:   capacity,
		loadFactor: loadFactor,
		threshold:  int(float32(capacity) * loadFactor),
	}
}

// Put agrega un nuevo par clave-valor a la tabla de hash. Si la clave ya
// existe, actualiza el valor asociado a la clave.
func (ht *HashTableOpenAddressing[K, V]) Put(key K, value V) {
	if index, esta := ht.getIndex(key); esta {
		ht.buckets[index].value = value
		return
	}

	if ht.size >= ht.threshold {
		ht.resize()
	}

	index := ht.hash(key) % ht.capacity
	for {
		if ht.buckets[index] == nil || ht.buckets[index].deleted {
			ht.buckets[index] = &hashTableEntry[K, V]{key: key, value: value}
			ht.size++
			return
		}
		index = (index + 1) % ht.capacity
	}
}

// Get devuelve el valor asociado a la clave y nil. Si la clave no existe,
// devuelve el zero value de V y un error.
func (ht *HashTableOpenAddressing[K, V]) Get(key K) (V, error) {
	index, exists := ht.getIndex(key)
	if !exists {
		var zero V
		return zero, errors.New("key not found")
	}
	return ht.buckets[index].value, nil
}

// Delete elimina el par clave-valor asociado a la clave.
// Devuelve error si la clave no existe.
//
// Usa eliminación perezosa (tombstone): marca la entrada como deleted en lugar
// de eliminarla del arreglo. Esto mantiene la continuidad de las sondas
// lineales: si se eliminara la entrada, las búsquedas posteriores podrían no
// encontrar elementos que están más allá en la secuencia de sondeo.
func (ht *HashTableOpenAddressing[K, V]) Delete(key K) error {
	index, exists := ht.getIndex(key)
	if !exists {
		return errors.New("key not found")
	}
	ht.buckets[index].deleted = true
	var zero V
	ht.buckets[index].value = zero
	ht.size--
	return nil
}

// Contains devuelve true si la clave existe en la tabla.
func (ht *HashTableOpenAddressing[K, V]) Contains(key K) bool {
	_, exists := ht.getIndex(key)
	return exists
}

// Keys devuelve una lista de todas las claves en la tabla de hash.
//
// Pre-asigna el slice con capacidad ht.size para evitar realocaciones durante
// los append. Solo incluye entradas activas (no eliminadas).
func (ht *HashTableOpenAddressing[K, V]) Keys() []K {
	keys := make([]K, 0, ht.size)
	for _, node := range ht.buckets {
		if node != nil && !node.deleted {
			keys = append(keys, node.key)
		}
	}
	return keys
}

// Values devuelve una lista de todos los valores en la tabla de hash.
//
// Pre-asigna el slice con capacidad ht.size para evitar realocaciones. Solo
// incluye valores de entradas activas (no eliminadas).
func (ht *HashTableOpenAddressing[K, V]) Values() []V {
	values := make([]V, 0, ht.size)
	for _, node := range ht.buckets {
		if node != nil && !node.deleted {
			values = append(values, node.value)
		}
	}
	return values
}

// Size devuelve el número de elementos en la tabla de hash.
func (ht *HashTableOpenAddressing[K, V]) Size() int {
	return ht.size
}

// IsEmpty devuelve true si la tabla de hash está vacía, false en caso contrario.
func (ht *HashTableOpenAddressing[K, V]) IsEmpty() bool {
	return ht.size == 0
}

// Clear elimina todos los elementos de la tabla de hash.
func (ht *HashTableOpenAddressing[K, V]) Clear() {
	ht.buckets = make([]*hashTableEntry[K, V], ht.capacity)
	ht.size = 0
}

// String devuelve una representación en cadena de la tabla de hash.
//
// Formato: {clave1: valor1, clave2: valor2}. Tras recorrer todas las entradas
// activas se elimina la última coma y espacio para mantener el formato limpio.
func (ht *HashTableOpenAddressing[K, V]) String() string {
	result := "{"
	for _, node := range ht.buckets {
		if node != nil && !node.deleted {
			result += fmt.Sprintf("%v: %v", node.key, node.value) + ", "
		}
	}
	if len(result) > 1 {
		result = result[:len(result)-2]
	}
	result += "}"
	return result
}
