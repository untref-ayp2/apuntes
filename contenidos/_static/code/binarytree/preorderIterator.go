package binarytree

import (
	"apunte/stack"
	"errors"

	"golang.org/x/exp/constraints"
)

type PreorderIterator[T constraints.Ordered] struct {
	stack *stack.Stack[*BinaryNode[T]]
}

func newPreorderIterator[T constraints.Ordered](root *BinaryNode[T]) *PreorderIterator[T] {
	// Crea un nuevo iterador de tipo PreorderIterator.
	it := &PreorderIterator[T]{}
	// Inicializa el iterador con la raíz del árbol y apila la raíz.
	it.stack = stack.NewStack[*BinaryNode[T]]()
	if root != nil {
		it.stack.Push(root)
	}
	// Devuelve el iterador inicializado.
	// Si la raíz es nula, la pila estará vacía y no habrá nodos para iterar.
	return it
}

// HasNext verifica si hay más elementos para iterar en el árbol.
func (it *PreorderIterator[T]) HasNext() bool {
	return !it.stack.IsEmpty()
}

// Next devuelve el siguiente elemento del árbol en order preorder.
func (it *PreorderIterator[T]) Next() (T, error) {
	if !it.HasNext() {
		var zero T
		return zero, errors.New("no hay más elementos para iterar")
	}

	// Obtener el nodo actual del tope de la pila.
	currentNode, _ := it.stack.Pop()

	// Apilar el hijo derecho primero, luego el izquierdo.
	if currentNode.GetRight() != nil {
		it.stack.Push(currentNode.GetRight())
	}

	if currentNode.GetLeft() != nil {
		it.stack.Push(currentNode.GetLeft())
	}

	// Devolver el dato del nodo actual.
	return currentNode.GetData(), nil
}
