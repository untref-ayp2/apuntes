package binarytree

import (
	"testing"
)

func TestPreorderIterator_EmptyTree(t *testing.T) {
	tree := NewBinarySearchTree[int]()
	it := tree.PreorderIterator()
	if it.HasNext() {
		t.Errorf("El iterador no debería tener elementos en un árbol vacío")
	}
	_, err := it.Next()
	if err == nil || err.Error() != "no hay más elementos para iterar" {
		t.Errorf("Se esperaba error 'no hay más elementos para iterar', se obtuvo: %v", err)
	}
}

func TestPreorderIterator_SingleNode(t *testing.T) {
	tree := NewBinarySearchTree[int]()
	tree.Insert(10)
	it := tree.PreorderIterator()
	if !it.HasNext() {
		t.Errorf("El iterador debería tener un elemento")
	}
	val, err := it.Next()
	if err != nil {
		t.Errorf("No se esperaba error, se obtuvo: %v", err)
	}
	if val != 10 {
		t.Errorf("Se esperaba 10, se obtuvo %d", val)
	}
	if it.HasNext() {
		t.Errorf("El iterador no debería tener más elementos")
	}
}

func TestPreorderIterator_MultipleNodes(t *testing.T) {
	tree := NewBinarySearchTree[int]()
	valores := []int{20, 10, 30, 5, 15, 25, 35}
	for _, v := range valores {
		tree.Insert(v)
	}
	it := tree.PreorderIterator()
	var resultado []int
	for it.HasNext() {
		val, err := it.Next()
		if err != nil {
			t.Errorf("No se esperaba error, se obtuvo: %v", err)
		}
		resultado = append(resultado, val)
	}
	esperado := []int{20, 10, 5, 15, 30, 25, 35}
	for i, v := range esperado {
		if resultado[i] != v {
			t.Errorf("En la posición %d, se esperaba %d, se obtuvo %d", i, v, resultado[i])
		}
	}
}

func TestPreorderIterator_NextAfterEnd(t *testing.T) {
	tree := NewBinarySearchTree[int]()
	tree.Insert(1)
	it := tree.PreorderIterator()
	_, err := it.Next()
	if err != nil {
		t.Errorf("No se esperaba error, se obtuvo: %v", err)
	}
	_, err = it.Next()
	if err == nil || err.Error() != "no hay más elementos para iterar" {
		t.Errorf("Se esperaba error 'no hay más elementos para iterar', se obtuvo: %v", err)
	}
}
