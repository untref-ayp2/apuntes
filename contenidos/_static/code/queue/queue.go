package queue

import "errors"

// Queue es una estructura de datos que implementa una cola genérica.
// Permite almacenar elementos de cualquier tipo y proporciona operaciones
// para agregar y eliminar elementos siguiendo el principio FIFO (First In, First Out).
type Queue[T any] struct {
	data []T
}

// NewQueue crea una nueva cola vacía.
func NewQueue[T any]() *Queue[T] {
	return &Queue[T]{data: []T{}}
}

// Enqueue agrega un elemento al final de la cola.
func (q *Queue[T]) Enqueue(element T) {
	q.data = append(q.data, element)
}

// Dequeue elimina y devuelve el elemento del frente de la cola.
// Devuelve un error si la cola está vacía.
func (q *Queue[T]) Dequeue() (T, error) {
	if len(q.data) == 0 {
		return *new(T), errors.New("la cola está vacía")
	}
	element := q.data[0]
	q.data = q.data[1:]
	return element, nil
}

// Front devuelve el elemento del frente de la cola sin eliminarlo.
// Devuelve un error si la cola está vacía.
func (q *Queue[T]) Front() (T, error) {
	if len(q.data) == 0 {
		return *new(T), errors.New("la cola está vacía")
	}
	return q.data[0], nil
}

// IsEmpty verifica si la cola está vacía.
func (q *Queue[T]) IsEmpty() bool {
	return len(q.data) == 0
}
