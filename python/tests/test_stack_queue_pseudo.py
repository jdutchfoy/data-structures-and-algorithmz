from stack_queue_pseudo import PseudoQueue

def test_pseudo_queue():
    pq = PseudoQueue()

    # Enqueue values
    pq.enqueue(1)
    pq.enqueue(2)
    pq.enqueue(3)

    # Dequeue values
    assert pq.dequeue() == 1
    assert pq.dequeue() == 2
    assert pq.dequeue() == 3

    # Check if queue is empty
    assert pq.stack_1.is_empty()
    assert pq.stack_2.is_empty()

    # Enqueue values again
    pq.enqueue(4)
    pq.enqueue(5)

    # Dequeue values again
    assert pq.dequeue() == 4
    assert pq.dequeue() == 5

    # Check if queue is empty again
    assert pq.stack_1.is_empty()
    assert pq.stack_2.is_empty()
