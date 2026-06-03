// hashtable define la interfaz HashTable y una implementación con hashing
// cerrado y sondeo lineal.
package hashtable

// HashTable define el contrato que deben implementar las tablas de hash.
//
// K debe ser un tipo comparable (puede usarse como clave en un map de Go).
// V puede ser cualquier tipo.
type HashTable[K comparable, V any] interface {
	// Put agrega un nuevo par clave-valor. Si la clave ya existe, actualiza
	// el valor asociado.
	Put(key K, value V)
	// Get devuelve el valor asociado a la clave.
	// Error si la clave no existe.
	Get(key K) (V, error)
	// Delete elimina el par clave-valor asociado a la clave.
	// Error si la clave no existe.
	Delete(key K) error
	// Contains devuelve true si la clave existe en la tabla.
	Contains(key K) bool
	// Size devuelve la cantidad de elementos en la tabla.
	Size() int
	// IsEmpty devuelve true si la tabla no tiene elementos.
	IsEmpty() bool
	// Keys devuelve una lista con todas las claves.
	Keys() []K
	// Values devuelve una lista con todos los valores.
	Values() []V
	// Clear elimina todos los elementos de la tabla.
	Clear()
	// String devuelve una representación en cadena estilo Python dict.
	// Formato: {clave1: valor1, clave2: valor2}
	String() string
}
