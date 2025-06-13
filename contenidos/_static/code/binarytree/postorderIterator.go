package binarytree

import (
	"apunte/stack"
	"errors"

	"golang.org/x/exp/constraints"
)

// PostorderIterator implementa un iterador para recorrer un árbol binario
// en postorder (postorden).
// Utiliza dos pilas para almacenar los nodos visitados y permite iterar sobre
// ellos en postorden, es decir, primero los hijos izquierdo y derecho, y
// finalmente el nodo padre.
type PostorderIterator[T constraints.Ordered] struct {
	stack1 *stack.Stack[*BinaryNode[T]]
	stack2 *stack.Stack[*BinaryNode[T]]
}

// newPostorderIterator crea un nuevo iterador para recorrer un árbol binario
// inicializa las pilas, apilando en la primera pila los nodos del árbol
func newPostorderIterator[T constraints.Ordered](root *BinaryNode[T]) *PostorderIterator[T] {
	it := &PostorderIterator[T]{
		stack1: stack.NewStack[*BinaryNode[T]](),
		stack2: stack.NewStack[*BinaryNode[T]](),
	}
	if root != nil {
		it.stack1.Push(root)
		for !it.stack1.IsEmpty() {
			node, _ := it.stack1.Pop()
			it.stack2.Push(node)
			if node.GetLeft() != nil {
				it.stack1.Push(node.GetLeft())
			}
			if node.GetRight() != nil {
				it.stack1.Push(node.GetRight())
			}
		}
	}
	return it
}

func (it *PostorderIterator[T]) HasNext() bool {
	return !it.stack2.IsEmpty()
}

func (it *PostorderIterator[T]) Next() (T, error) {
	var zero T
	if it.stack2.IsEmpty() {
		return zero, errors.New("no hay más elementos para iterar")
	}
	node, _ := it.stack2.Pop()
	return node.GetData(), nil
}
