package binarytree
import (
	"testing"
)

func TestPostorderIterator_EmptyTree(t *testing.T) {
	bst := NewBinarySearchTree[int]()
	it := bst.PostorderIterator()
	if it.HasNext() {
		t.Error("Expected HasNext to be false for empty tree")
	}
	_, err := it.Next()
	if err == nil {
		t.Error("Expected error when calling Next on empty iterator")
	}
}

func TestPostorderIterator_SingleNode(t *testing.T) {
	bst := NewBinarySearchTree[int]()
	bst.Insert(10)
	it := bst.PostorderIterator()
	if !it.HasNext() {
		t.Error("Expected HasNext to be true for single node")
	}
	val, err := it.Next()
	if err != nil {
		t.Errorf("Unexpected error: %v", err)
	}
	if val != 10 {
		t.Errorf("Expected 10, got %v", val)
	}
	if it.HasNext() {
		t.Error("Expected HasNext to be false after consuming single node")
	}
}

func TestPostorderIterator_TwoLevels(t *testing.T) {
	bst := NewBinarySearchTree[int]()
	bst.Insert(2)
	bst.Insert(1)
	bst.Insert(3)
	it := bst.PostorderIterator()
	var got []int
	for it.HasNext() {
		val, err := it.Next()
		if err != nil {
			t.Fatalf("Unexpected error: %v", err)
		}
		got = append(got, val)
	}
	// The implemented iterator is not a true postorder, but a root-right-left traversal.
	// So the expected order is: 1, 3, 2
	expected := []int{1, 3, 2}
	for i, v := range expected {
		if got[i] != v {
			t.Errorf("Expected %d at position %d, got %d", v, i, got[i])
		}
	}
}

func TestPostorderIterator_LeftSkewed(t *testing.T) {
	bst := NewBinarySearchTree[int]()
	bst.Insert(3)
	bst.Insert(2)
	bst.Insert(1)
	it := bst.PostorderIterator()
	var got []int
	for it.HasNext() {
		val, err := it.Next()
		if err != nil {
			t.Fatalf("Unexpected error: %v", err)
		}
		got = append(got, val)
	}
	expected := []int{1, 2, 3}
	for i, v := range expected {
		if got[i] != v {
			t.Errorf("Expected %d at position %d, got %d", v, i, got[i])
		}
	}
}

func TestPostorderIterator_RightSkewed(t *testing.T) {
	bst := NewBinarySearchTree[int]()
	bst.Insert(1)
	bst.Insert(2)
	bst.Insert(3)
	it := bst.PostorderIterator()

	var got []int
	for it.HasNext() {
		val, err := it.Next()
		if err != nil {
			t.Fatalf("Unexpected error: %v", err)
		}
		got = append(got, val)
	}
	expected := []int{3, 2, 1}
	for i, v := range expected {
		if got[i] != v {
			t.Errorf("Expected %d at position %d, got %d", v, i, got[i])
		}
	}
}

func TestPostorderIterator_FullBST(t *testing.T) {
	bst := NewBinarySearchTree[int]()
	bst.Insert(5)
	bst.Insert(1)
	bst.Insert(9)
	bst.Insert(4)
	bst.Insert(2)
	bst.Insert(6)
	bst.Insert(10)
	bst.Insert(7)
	bst.Insert(8)
	bst.Insert(3)
	it := bst.PostorderIterator()
	var got []int
	for it.HasNext() {
		val, err := it.Next()
		if err != nil {
			t.Fatalf("Unexpected error: %v", err)
		}
		got = append(got, val)
	}
	expected := []int{3, 2, 4, 1, 8, 7, 6, 10, 9, 5}
	for i, v := range expected {
		if got[i] != v {
			t.Errorf("Expected %d at position %d, got %d", v, i, got[i])
		}
	}
}