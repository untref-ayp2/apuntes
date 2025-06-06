package stack

import (
	"testing"
)

func TestPushAndPop(t *testing.T) {
	var s Stack[int]
	s.Push(10)
	s.Push(20)
	s.Push(30)

	val, err := s.Pop()
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if val != 30 {
		t.Errorf("expected 30, got %d", val)
	}

	val, err = s.Pop()
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if val != 20 {
		t.Errorf("expected 20, got %d", val)
	}

	val, err = s.Pop()
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if val != 10 {
		t.Errorf("expected 10, got %d", val)
	}

	_, err = s.Pop()
	if err == nil {
		t.Error("expected error when popping from empty stack, got nil")
	}
}

func TestPeek(t *testing.T) {
	var s Stack[string]
	s.Push("a")
	s.Push("b")

	val, err := s.Peek()
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if val != "b" {
		t.Errorf("expected 'b', got %s", val)
	}

	// Peek should not remove the element
	val2, err := s.Peek()
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if val2 != "b" {
		t.Errorf("expected 'b', got %s", val2)
	}
}

func TestIsEmpty(t *testing.T) {
	var s Stack[float64]
	if !s.IsEmpty() {
		t.Error("expected stack to be empty")
	}
	s.Push(1.1)
	if s.IsEmpty() {
		t.Error("expected stack to be non-empty")
	}
	s.Pop()
	if !s.IsEmpty() {
		t.Error("expected stack to be empty after pop")
	}
}

func TestPopEmptyStack(t *testing.T) {
	var s Stack[int]
	_, err := s.Pop()
	if err == nil {
		t.Error("expected error when popping from empty stack, got nil")
	}
}

func TestPeekEmptyStack(t *testing.T) {
	var s Stack[int]
	_, err := s.Peek()
	if err == nil {
		t.Error("expected error when peeking from empty stack, got nil")
	}
}

