package binarytree

import (
	"apunte/stack"
	"errors"

	"golang.org/x/exp/constraints"
)

// InorderIterator implementa un iterador para recorrer un árbol binario de
// búsqueda en order (inorder).
// Utiliza una pila para almacenar los nodos visitados y permite iterar sobre
// ellos en order ascendente.
type InorderIterator[T constraints.Ordered] struct {
	stack *stack.Stack[*BinaryNode[T]]
}

func newInorderIterator[T constraints.Ordered](root *BinaryNode[T]) *InorderIterator[T] {
	// Crea un nuevo iterador de tipo InorderIterator.
	it := &InorderIterator[T]{}
	// Inicializa el iterador con la raíz del árbol y apila todos los nodos
	// izquierdos.
	it.stack = stack.NewStack[*BinaryNode[T]]()
	if root != nil {
		it.pushLeftNodes(root)
	}
	// Devuelve el iterador inicializado.
	// Si la raíz es nula, la pila estará vacía y no habrá nodos para iterar.
	return it
}

// pushLeftNodes apila todos los nodos izquierdos desde un nodo dado.
// Parámetros:
//   - node: un puntero al nodo desde el cual comenzar a apilar los nodos
//
// izquierdos.
func (it *InorderIterator[T]) pushLeftNodes(node *BinaryNode[T]) {
	for node != nil {
		it.stack.Push(node)
		node = node.GetLeft()
	}
}

// HasNext verifica si hay más elementos para iterar en el árbol.
// Retorna:
//   - true si hay más elementos, false en caso contrario.
func (it *InorderIterator[T]) HasNext() bool {
	return !it.stack.IsEmpty()
}

// Next devuelve el siguiente elemento del árbol en order inorder.
// La semántica de Next consiste en avanzar primero al siguiente
// elemento y luego devolverlo. Si no hay más elementos, devuelve un error.
// Retorna:
//   - el siguiente elemento del tipo T en el árbol.
//   - un error si no hay más elementos para iterar.
func (it *InorderIterator[T]) Next() (T, error) {
	if !it.HasNext() {
		var zero T // Valor cero para el tipo T
		return zero, errors.New("no hay más elementos para iterar")
	}

	// Obtener el nodo actual del tope de la pila.
	currentNode, _ := it.stack.Pop()

	// Apilar los nodos izquierdos del hijo derecho del nodo actual.
	it.pushLeftNodes(currentNode.GetRight())

	// Devolver el dato del nodo actual.
	return currentNode.GetData(), nil
}
