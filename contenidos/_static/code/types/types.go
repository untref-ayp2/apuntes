package types

// Iterator es una interfaz genérica que define un iterador para colecciones.
type Iterator[T any] interface {
	HasNext() bool
	Next() (T, error)
}
