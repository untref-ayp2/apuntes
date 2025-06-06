package binarytree

import (
	"apunte/stack"
	"errors"
	"golang.org/x/exp/constraints"
)

// PostorderIterator implementa un iterador para recorrer un árbol binario de búsqueda en order postorder.
type PostorderIterator[T constraints.Ordered] struct {
	stack *stack.Stack[*BinaryNode[T]]
	ultimoVisitado *BinaryNode[T] // Último nodo visitado en el recorrido postorder
}

// setup inicializa el iterador con la raíz del árbol y apila todos los nodos izquierdos.
func (it *PostorderIterator[T]) setup(root *BinaryNode[T]) {
	it.stack = stack.NewStack[*BinaryNode[T]]()
	it.pushLeftNodes(root)
	it.ultimoVisitado = nil // Inicializar el último nodo visitado como nil
}

// pushLeftNodes apila todos los nodos izquierdos del árbol.
func (it *PostorderIterator[T]) pushLeftNodes(node *BinaryNode[T]) {
	for node != nil {
		it.stack.Push(node)
		node = node.GetLeft()
	}
}

// HasNext verifica si hay más elementos para iterar en el árbol.
// Retorna:
//   - true si hay más elementos, false en caso contrario.
func (it *PostorderIterator[T]) HasNext() bool {
	return !it.stack.IsEmpty()
}

// Next devuelve el siguiente elemento del árbol en order postorder.
// La semántica de Next consiste en avanzar primero al siguiente
// elemento y luego devolverlo. Si no hay más elementos, devuelve un error.
// Retorna:
//   - el siguiente elemento del tipo T en el árbol.
//   - un error si no hay más elementos para iterar.
func (it *PostorderIterator[T]) Next() (T, error) {
	if !it.HasNext() {
		var zero T // Valor cero para el tipo T
		return zero, errors.New("no hay más elementos para iterar")
	}

	// Obtener el nodo actual del tope de la pila.
	currentNode, _ := it.stack.Pop()

	// Si el nodo tiene un hijo derecho que no ha sido visitado, apilarlo.
	if currentNode.GetRight() != nil && currentNode.GetRight() != it.ultimoVisitado {
		it.stack.Push(currentNode)
		it.pushLeftNodes(currentNode.GetRight())
		return it.Next() // Llamar recursivamente para obtener el siguiente nodo
	}

	// Marcar el nodo actual como visitado.
	it.ultimoVisitado = currentNode

	// Devolver el dato del nodo actual.
	return currentNode.GetData(), nil
}