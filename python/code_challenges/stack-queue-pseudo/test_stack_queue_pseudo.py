
    # Test enqueue and dequeue of one element
pq.enqueue(1)
assert pq.dequeue() == 1

    # Test enqueue and dequeue of multiple elements
pq.enqueue(2)
pq.enqueue(3)
pq.enqueue(4)
assert pq.dequeue() == 2
assert pq.dequeue() == 3
assert pq.dequeue() == 4
     # Test enqueue after dequeue
pq.enqueue(5)
assert pq.dequeue() == 5

    # Test dequeue from empty queue
assert pq.dequeue() is None

    # Test enqueue and dequeue of strings
pq.enqueue("hello")
pq.enqueue("world")
assert pq.dequeue() == "hello"
assert pq.dequeue() == "world"


if __name__ == "__main__":
    test_pseudo_queue()