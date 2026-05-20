package stack

import "errors"

// Stack es una estructura de datos que implementa una pila genérica.
// Permite almacenar elementos de cualquier tipo y proporciona operaciones
// para agregar y eliminar elementos siguiendo el principio LIFO (Last In, First Out).
type Stack[T any] struct {
	data []T
}

func NewStack[T any]() *Stack[T] {
	return &Stack[T]{data: []T{}}
}

// Push agrega un elemento a la parte superior de la pila.
func (s *Stack[T]) Push(element T) {
	s.data = append(s.data, element)
}

// Pop elimina y devuelve el elemento de la parte superior de la pila.
// Devuelve un error si la pila está vacía.
func (s *Stack[T]) Pop() (T, error) {
	if len(s.data) == 0 {
		return *new(T), errors.New("la pila está vacía")
	}
	element := s.data[len(s.data)-1]
	s.data = s.data[:len(s.data)-1]
	return element, nil
}

// Top devuelve el elemento de la parte superior de la pila sin eliminarlo.
// Devuelve un error si la pila está vacía.
func (s *Stack[T]) Top() (T, error) {
	if len(s.data) == 0 {
		return *new(T), errors.New("la pila está vacía")
	}
	return s.data[len(s.data)-1], nil
}

// IsEmpty verifica si la pila está vacía.
func (s *Stack[T]) IsEmpty() bool {
	return len(s.data) == 0
}
