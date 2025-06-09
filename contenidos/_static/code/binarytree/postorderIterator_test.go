package binarytree

import (
	"testing"
)

func TestPostorderIterator_EmptyTree(t *testing.T) {
	tree := NewBinarySearchTree[int]()
	it := tree.PostorderIterator()
	if it.HasNext() {
		t.Error("El iterador no debería tener siguiente en un árbol vacío")
	}
	_, err := it.Next()
	if err == nil {
		t.Error("Se esperaba un error al llamar Next() en un iterador vacío")
	}
}

func TestPostorderIterator_SingleNode(t *testing.T) {
	tree := NewBinarySearchTree[int]()
	tree.Insert(10)
	it := tree.PostorderIterator()
	if !it.HasNext() {
		t.Error("El iterador debería tener siguiente para un árbol con un solo nodo")
	}
	val, err := it.Next()
	if err != nil {
		t.Errorf("Error inesperado: %v", err)
	}
	if val != 10 {
		t.Errorf("Se esperaba 10, se obtuvo %v", val)
	}
	if it.HasNext() {
		t.Error("El iterador no debería tener siguiente después de un solo elemento")
	}
}

func TestPostorderIterator_MultipleNodes(t *testing.T) {
	tree := NewBinarySearchTree[int]()
	values := []int{20, 10, 30, 5, 15, 25, 35}
	for _, v := range values {
		tree.Insert(v)
	}
	it := tree.PostorderIterator()
	var got []int
	for it.HasNext() {
		val, err := it.Next()
		if err != nil {
			t.Fatalf("Error inesperado: %v", err)
		}
		got = append(got, val)
	}
	// Postorden: izquierda, derecha, raíz
	want := []int{5, 15, 10, 25, 35, 30, 20}
	for i, v := range want {
		if got[i] != v {
			t.Errorf("En el índice %d: se esperaba %d, se obtuvo %d", i, v, got[i])
		}
	}
}

func TestPostorderIterator_NextAfterEnd(t *testing.T) {
	tree := NewBinarySearchTree[int]()
	tree.Insert(1)
	it := tree.PostorderIterator()
	_, err := it.Next()
	if err != nil {
		t.Errorf("Error inesperado: %v", err)
	}
	_, err = it.Next()
	if err == nil {
		t.Error("Se esperaba un error al llamar Next() después del final")
	}
}
