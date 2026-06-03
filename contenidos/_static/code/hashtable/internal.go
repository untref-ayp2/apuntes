package hashtable

import "fmt"

// a es una constante utilizada para calcular el hash de un string
const a int = 11

// hash calcula el índice del bucket para una clave dada.
//
// Se utiliza la técnica de Multiplicación Polinómica con el método de Horner:
// evalúa el polinomio c1*a^{n-1} + c2*a^{n-2} + ... + cn*a^0 aplicando
// la propiedad distributiva para evitar el cálculo costoso de potencias.
//
// La constante a=11 es un número primo pequeño que ofrece buena dispersión
// para cadenas de texto.
//
// Como K es cualquier tipo comparable, se convierte la clave a string con
// fmt.Sprintf para aplicar el algoritmo polinómico sobre su representación.
//
// El módulo por la capacidad NO se aplica acá sino en el llamante, para que
// este mismo valor pueda reusarse al buscar en distintas capacidades (ej.
// durante el redimensionamiento).
func (ht *HashTableOpenAddressing[K, V]) hash(key K) int {
	s := fmt.Sprintf("%v", key)
	var hash int = 0
	for _, c := range s {
		hash = hash*a + int(c)
	}
	return hash
}

// getIndex devuelve el índice del bucket para una clave dada y un booleano que
// indica si la clave existe.
//
// Realiza una sonda lineal (linear probing): calcula el índice inicial con
// hash(key) % capacity y, si el bucket está ocupado por otra clave, avanza
// secuencialmente hasta encontrar la clave buscada o un bucket vacío (nil).
//
// La condición i < ht.capacity limita la búsqueda para evitar un bucle
// infinito si la tabla estuviera completamente llena (sin buckets nil).
// Al encontrar un bucket nil detiene la búsqueda porque en hashing cerrado
// con sondeo lineal los elementos no saltan buckets vacíos.
func (ht *HashTableOpenAddressing[K, V]) getIndex(key K) (int, bool) {
	for i, index := 0, ht.hash(key)%ht.capacity; i < ht.capacity && ht.buckets[index] != nil; i, index = i+1, (index+1)%ht.capacity {
		if !ht.buckets[index].deleted && ht.buckets[index].key == key {
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
//
// Se itera sobre todos los buckets del arreglo viejo y se reinsertan solo las
// entradas activas (no eliminadas). Las entradas marcadas como deleted se
// descartan, liberando así la memoria que ocupaban.
//
// Tras la reubicación se actualizan capacity y threshold. El factor de carga
// loadFactor se mantiene igual. Esto asegura que la próxima vez que se alcance
// el umbral se vuelva a redimensionar.
func (ht *HashTableOpenAddressing[K, V]) resize() {
	newCapacity := nextPrime(ht.capacity * 2)
	newBuckets := make([]*hashTableEntry[K, V], newCapacity)

	for _, node := range ht.buckets {
		if node != nil && !node.deleted {
			index := ht.hash(node.key) % newCapacity
			for newBuckets[index] != nil {
				index = (index + 1) % newCapacity
			}
			newBuckets[index] = node
		}
	}

	ht.buckets = newBuckets
	ht.capacity = newCapacity
	ht.threshold = int(float32(newCapacity) * ht.loadFactor)
}

// nextPrime devuelve el siguiente número primo mayor o igual a n.
//
// La búsqueda es secuencial: prueba cada número a partir de n hacia arriba
// hasta encontrar un primo. Como la frecuencia de primos es aproximadamente
// n / ln(n), rara vez recorre muchos números.
func nextPrime(n int) int {
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
//
// Optimización 6k ± 1: todo primo mayor a 3 puede expresarse como 6k ± 1.
// Esto permite verificar divisibilidad solo con números de esa forma,
// reduciendo las iteraciones a ~1/3 de una verificación ingenua.
func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	if n <= 3 {
		return true
	}
	if n%2 == 0 || n%3 == 0 {
		return false
	}
	for i := 5; i*i <= n; i += 6 {
		if n%i == 0 || n%(i+2) == 0 {
			return false
		}
	}
	return true
}
