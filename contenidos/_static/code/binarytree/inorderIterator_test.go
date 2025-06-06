package binarytree
import (
	"testing"
)

func TestInorderIterator_EmptyTree(t *testing.T) {
	bst := NewBinarySearchTree[int]()
	iter := bst.InorderIterator()
	if iter.HasNext() {
		t.Error("HasNext() should be false for empty tree")
	}
	_, err := iter.Next()
	if err == nil {
		t.Error("Next() should return error for empty tree")
	}
}

func TestInorderIterator_SingleNode(t *testing.T) {
	bst := NewBinarySearchTree[int]()
	bst.Insert(42)
	
	iter := bst.InorderIterator()
	if !iter.HasNext() {
		t.Error("HasNext() should be true for single node tree")
	}
	val, err := iter.Next()
	if err != nil {
		t.Errorf("Next() returned unexpected error: %v", err)
	}
	if val != 42 {
		t.Errorf("Expected 42, got %d", val)
	}
	if iter.HasNext() {
		t.Error("HasNext() should be false after consuming single node")
	}
}

func TestInorderIterator_FullBST(t *testing.T) {
	// Construye el siguiente árbol BST usando BinarySearchTree:
	//        4
	//      /   \
	//     2     6
	//    / \   / \
	//   1   3 5   7
	bst := NewBinarySearchTree[int]()
	bst.Insert(4)
	bst.Insert(2)
	bst.Insert(6)
	bst.Insert(1)
	bst.Insert(3)
	bst.Insert(5)
	bst.Insert(7)

	iter := bst.InorderIterator()
	expected := []int{1, 2, 3, 4, 5, 6, 7}
	var result []int
	for iter.HasNext() {
		val, err := iter.Next()
		if err != nil {
			t.Fatalf("Unexpected error: %v", err)
		}
		result = append(result, val)
	}
	if len(result) != len(expected) {
		t.Fatalf("Expected %d elements, got %d", len(expected), len(result))
	}
	for i, v := range expected {
		if result[i] != v {
			t.Errorf("At index %d: expected %d, got %d", i, v, result[i])
		}
	}
}

func TestInorderIterator_NextAfterEnd(t *testing.T) {
	bst := NewBinarySearchTree[int]()
	bst.Insert(4)
	bst.Insert(2)
	bst.Insert(6)
	bst.Insert(1)
	bst.Insert(3)
	bst.Insert(5)
	bst.Insert(7)

	iter := bst.InorderIterator()
	for iter.HasNext() {
		_, err := iter.Next()
		if err != nil {
			t.Fatalf("Unexpected error: %v", err)
		}
	}
	_, err := iter.Next()
	if err == nil {
		t.Error("Next() should return error after iteration ends")
	}
}

func TestInorderIterator_LeftSkewedTree(t *testing.T) {
	// Tree: 3 <- 2 <- 1
	bst := NewBinarySearchTree[int]()
	bst.Insert(3)
	bst.Insert(2)
	bst.Insert(1)
	iter := bst.InorderIterator()
	expected := []int{1, 2, 3}
	for _, v := range expected {
		if !iter.HasNext() {
			t.Fatalf("Expected HasNext() true for value %d", v)
		}
		val, err := iter.Next()
		if err != nil {
			t.Fatalf("Unexpected error: %v", err)
		}
		if val != v {
			t.Errorf("Expected %d, got %d", v, val)
		}
	}
	if iter.HasNext() {
		t.Error("HasNext() should be false after all elements")
	}
}

func TestInorderIterator_RightSkewedTree(t *testing.T) {
	// Tree: 1 -> 2 -> 3
	bst := NewBinarySearchTree[int]()
	bst.Insert(1)
	bst.Insert(2)
	bst.Insert(3)
	iter := bst.InorderIterator()
	expected := []int{1, 2, 3}
	for _, v := range expected {
		if !iter.HasNext() {
			t.Fatalf("Expected HasNext() true for value %d", v)
		}
		val, err := iter.Next()
		if err != nil {
			t.Fatalf("Unexpected error: %v", err)
		}
		if val != v {
			t.Errorf("Expected %d, got %d", v, val)
		}
	}
	if iter.HasNext() {
		t.Error("HasNext() should be false after all elements")
	}
}
