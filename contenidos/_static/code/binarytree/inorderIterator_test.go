package binarytree

import (
	"testing"
)

func TestInorderIterator_EmptyTree(t *testing.T) {
	tree := NewBinarySearchTree[int]()
	it := tree.InorderIterator()
	if it.HasNext() {
		t.Error("Se esperaba que HasNext() fuera falso para un árbol vacío")
	}
	_, err := it.Next()
	if err == nil {
		t.Error("Se esperaba un error al llamar a Next() en un iterador vacío")
	}
}

func TestInorderIterator_SingleNode(t *testing.T) {
	tree := NewBinarySearchTree[int]()
	tree.Insert(10)
	it := tree.InorderIterator()
	if !it.HasNext() {
		t.Error("Se esperaba que HasNext() fuera verdadero para un árbol con un solo nodo")
	}
	val, err := it.Next()
	if err != nil {
		t.Errorf("Error inesperado: %v", err)
	}
	if val != 10 {
		t.Errorf("Se esperaba 10, se obtuvo %v", val)
	}
	if it.HasNext() {
		t.Error("Se esperaba que HasNext() fuera falso después de un solo elemento")
	}
}

func TestInorderIterator_MultipleNodes(t *testing.T) {
	tree := NewBinarySearchTree[int]()
	values := []int{20, 10, 30, 5, 15, 25, 35}
	for _, v := range values {
		tree.Insert(v)
	}
	it := tree.InorderIterator()
	expected := []int{5, 10, 15, 20, 25, 30, 35}
	var result []int
	for it.HasNext() {
		val, err := it.Next()
		if err != nil {
			t.Fatalf("Error inesperado: %v", err)
		}
		result = append(result, val)
	}
	for i, v := range expected {
		if result[i] != v {
			t.Errorf("Se esperaba %d en la posición %d, se obtuvo %d", v, i, result[i])
		}
	}
}

func TestInorderIterator_NextAfterEnd(t *testing.T) {
	tree := NewBinarySearchTree[int]()
	tree.Insert(1)
	it := tree.InorderIterator()
	_, err := it.Next()
	if err != nil {
		t.Errorf("Error inesperado: %v", err)
	}
	_, err = it.Next()
	if err == nil {
		t.Error("Se esperaba un error al llamar a Next() después del final")
	}
}
