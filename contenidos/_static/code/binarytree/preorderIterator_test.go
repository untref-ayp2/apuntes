package binarytree
import (
	"testing"
)
func TestPreorderIterator_EmptyTree(t *testing.T) {
	var root *BinaryNode[int] = nil
	var it PreorderIterator[int]
	it.setup(root)

	if it.HasNext() {
		t.Error("Expected HasNext to be false for empty tree")
	}
	_, err := it.Next()
	if err == nil {
		t.Error("Expected error when calling Next on empty tree")
	}
}

func TestPreorderIterator_SingleNode(t *testing.T) {
	root := &BinaryNode[int]{data: 10}
	var it PreorderIterator[int]
	it.setup(root)

	if !it.HasNext() {
		t.Error("Expected HasNext to be true for single node tree")
	}
	val, err := it.Next()
	if err != nil {
		t.Errorf("Unexpected error: %v", err)
	}
	if val != 10 {
		t.Errorf("Expected 10, got %v", val)
	}
	if it.HasNext() {
		t.Error("Expected HasNext to be false after single Next")
	}
}

func TestPreorderIterator_TwoLevels(t *testing.T) {
	bst := NewBinarySearchTree[int]()
	bst.Insert(2)
	bst.Insert(1)
	bst.Insert(3)
	it := bst.PreorderIterator()

	expected := []int{2, 1, 3}
	if !it.HasNext() {
		t.Error("Expected HasNext to be true for two-level tree")
	}
	var got []int
	for it.HasNext() {
		val, err := it.Next()
		if err != nil {
			t.Fatalf("Unexpected error: %v", err)
		}
		got = append(got, val)
	}
	for i, v := range expected {
		if got[i] != v {
			t.Errorf("Expected %d at position %d, got %d", v, i, got[i])
		}
	}
	if it.HasNext() {
		t.Error("Expected HasNext to be false after consuming all nodes")
	}
}

func TestPreorderIterator_LeftSkewed(t *testing.T) {
	root := &BinaryNode[int]{data: 1}
	root.left = &BinaryNode[int]{data: 2}
	root.left.left = &BinaryNode[int]{data: 3}

	var it PreorderIterator[int]
	it.setup(root)

	expected := []int{1, 2, 3}
	for i, v := range expected {
		val, err := it.Next()
		if err != nil {
			t.Errorf("Unexpected error at step %d: %v", i, err)
		}
		if val != v {
			t.Errorf("Expected %d, got %v at step %d", v, val, i)
		}
	}
}

func TestPreorderIterator_RightSkewed(t *testing.T) {
	root := &BinaryNode[int]{data: 1}
	root.right = &BinaryNode[int]{data: 2}
	root.right.right = &BinaryNode[int]{data: 3}

	var it PreorderIterator[int]
	it.setup(root)

	expected := []int{1, 2, 3}
	for i, v := range expected {
		val, err := it.Next()
		if err != nil {
			t.Errorf("Unexpected error at step %d: %v", i, err)
		}
		if val != v {
			t.Errorf("Expected %d, got %v at step %d", v, val, i)
		}
	}
}

func TestPreorderIterator_FullBST(t *testing.T) {
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
	it := bst.PreorderIterator()
	var got []int
	for it.HasNext() {
		val, err := it.Next()
		if err != nil {
			t.Fatalf("Unexpected error: %v", err)
		}
		got = append(got, val)
	}
	expected := []int{5, 1, 4, 2, 3, 9, 6, 7, 8, 10}
	for i, v := range expected {
		if got[i] != v {
			t.Errorf("Expected %d at position %d, got %d", v, i, got[i])
		}
	}
}
