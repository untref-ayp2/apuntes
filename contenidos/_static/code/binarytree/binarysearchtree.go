package binarytree

import (
	"apunte/types"

	"golang.org/x/exp/constraints"
)

// BinarySearchTree implementa un árbol binario de búsqueda
// (Binary Search Tree, BST).
// El árbol está compuesto por nodos de tipo BinaryNode, que contienen un valor
// de tipo T generico pero Ordered.
type BinarySearchTree[T constraints.Ordered] struct {
	root *BinaryNode[T]
}

// NewBinarySearchTree crea un nuevo BinarySearchTree de tipo Ordered.
//
// Uso:
//
//	bst := tree.NewBinarySearchTree[int]()
//
// Retorna:
//   - un puntero a un nuevo BinarySearchTree.
func NewBinarySearchTree[T constraints.Ordered]() *BinarySearchTree[T] {
	return &BinarySearchTree[T]{root: nil}
}

// GetRoot obtiene el nodo raíz del árbol.
//
// Uso:
//
//	bst := tree.NewBinarySearchTree[int]()
//	bst.GetRoot()
//
// Retorna:
//   - un puntero al nodo raíz del árbol.
func (bst *BinarySearchTree[T]) GetRoot() *BinaryNode[T] {
	return bst.root
}

// Insert inserta un nuevo nodo en el árbol.
//
// Uso:
//
//	bst := tree.NewBinarySearchTree[int]()
//	bst.Insert(4)
//
// Parámetros:
//   - `k` un valor de tipo T.
func (bst *BinarySearchTree[T]) Insert(k T) {
	bst.root = bst.insertByNode(bst.root, k)
}

// insertByNode inserta un nuevo nodo en el árbol.
//
// Parámetros:
//   - `node` un puntero a un BinaryNode.
//   - `k` un valor de tipo T.
//
// Retorna:
//   - un puntero al nodo raíz del árbol.
func (bst *BinarySearchTree[T]) insertByNode(
	node *BinaryNode[T], k T) *BinaryNode[T] {

	if node == nil {
		return NewBinaryNode(k, nil, nil)
	}

	if k < node.data {
		node.left = bst.insertByNode(node.left, k)
	} else if k > node.data {
		node.right = bst.insertByNode(node.right, k)
	}
	return node
}

func (bst *BinarySearchTree[T]) Clear() {
	bst.root = nil
}

// IsEmpty evalúa si el árbol está vacío.
//
// Uso:
//
//	bst := tree.NewBinarySearchTree[int]()
//	bst.IsEmpty()
//
// Retorna:
//   - `true` si el árbol está vacío; `false` si no lo está.
func (bst *BinarySearchTree[T]) IsEmpty() bool {
	return bst.root == nil
}

func (bst *BinarySearchTree[T]) InorderIterator() types.Iterator[T] {
	iter := newInorderIterator(bst.root)
	return iter
}

func (bst *BinarySearchTree[T]) PreorderIterator() types.Iterator[T] {
	iter := newPreorderIterator(bst.root)
	return iter
}

func (bst *BinarySearchTree[T]) PostorderIterator() types.Iterator[T] {
	iter := newPostorderIterator(bst.root)
	return iter
}
