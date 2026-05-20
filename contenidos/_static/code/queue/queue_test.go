package queue

import (
	"testing"
)

func TestEnqueueAndDequeue(t *testing.T) {
	var q Queue[int]
	q.Enqueue(10)
	q.Enqueue(20)
	q.Enqueue(30)

	val, err := q.Dequeue()
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if val != 10 {
		t.Errorf("expected 10, got %d", val)
	}

	val, err = q.Dequeue()
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if val != 20 {
		t.Errorf("expected 20, got %d", val)
	}

	val, err = q.Dequeue()
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if val != 30 {
		t.Errorf("expected 30, got %d", val)
	}

	_, err = q.Dequeue()
	if err == nil {
		t.Error("expected error when dequeuing from empty queue, got nil")
	}
}

func TestFront(t *testing.T) {
	var q Queue[string]
	q.Enqueue("a")
	q.Enqueue("b")

	val, err := q.Front()
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if val != "a" {
		t.Errorf("expected 'a', got %s", val)
	}

	// Front should not remove the element
	val2, err := q.Front()
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if val2 != "a" {
		t.Errorf("expected 'a', got %s", val2)
	}
}

func TestIsEmpty(t *testing.T) {
	var q Queue[float64]
	if !q.IsEmpty() {
		t.Error("expected queue to be empty")
	}
	q.Enqueue(1.1)
	if q.IsEmpty() {
		t.Error("expected queue to be non-empty")
	}
	q.Dequeue()
	if !q.IsEmpty() {
		t.Error("expected queue to be empty after dequeue")
	}
}

func TestDequeueEmptyQueue(t *testing.T) {
	var q Queue[int]
	_, err := q.Dequeue()
	if err == nil {
		t.Error("expected error when dequeuing from empty queue, got nil")
	}
}

func TestFrontEmptyQueue(t *testing.T) {
	var q Queue[int]
	_, err := q.Front()
	if err == nil {
		t.Error("expected error when front on empty queue, got nil")
	}
}
