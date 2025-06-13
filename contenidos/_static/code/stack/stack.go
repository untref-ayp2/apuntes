package stack

import "errors"

// Stack es una estructura de datos que implementa una pila genérica.
// Permite almacenar elementos de cualquier tipo y proporciona operaciones
// para agregar y eliminar elementos siguiendo el principio LIFO (Last In, First Out).
type Stack[T any] struct {
	elements []T
}

func NewStack[T any]() *Stack[T] {
	return &Stack[T]{elements: []T{}}
}

// Push agrega un elemento a la parte superior de la pila.
func (s *Stack[T]) Push(element T) {
	s.elements = append(s.elements, element)
}

// Pop elimina y devuelve el elemento de la parte superior de la pila.
// Devuelve un error si la pila está vacía.
func (s *Stack[T]) Pop() (T, error) {
	if len(s.elements) == 0 {
		return *new(T), errors.New("la pila está vacía")
	}
	element := s.elements[len(s.elements)-1]
	s.elements = s.elements[:len(s.elements)-1]
	return element, nil
}

// Peek devuelve el elemento de la parte superior de la pila sin eliminarlo.
// Devuelve un error si la pila está vacía.
func (s *Stack[T]) Peek() (T, error) {
	if len(s.elements) == 0 {
		return *new(T), errors.New("la pila está vacía")
	}
	return s.elements[len(s.elements)-1], nil
}

// IsEmpty verifica si la pila está vacía.
func (s *Stack[T]) IsEmpty() bool {
	return len(s.elements) == 0
}