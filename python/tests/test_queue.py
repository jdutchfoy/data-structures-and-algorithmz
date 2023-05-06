from queue import Queue
    # Test the Queue class
def test_queue():
    # Create an empty queue
    q = Queue()

    # Test enqueueing into a queue
    q.enqueue(1)
    assert q.items == [1]

    # Test enqueueing multiple values into a queue
    q.enqueue(2)
    q.enqueue(3)
    assert q.items == [1, 2, 3]

    # Test dequeuing out of a queue the expected value
    assert q.dequeue() == 1
    assert q.items == [2, 3]

    # Test peeking into a queue, seeing the expected value
    assert q.peek() == 2

    # Test emptying a queue after multiple dequeues
    q.dequeue()
    q.dequeue()
    assert q.is_empty() == True

    # Test instantiating an empty queue
    q = Queue()
    assert q.is_empty() == True

    # Test calling dequeue or peek on empty queue raises exception
    try:
        q.dequeue()
        assert False
    except ValueError as e:
        assert str(e) == "Cannot dequeue from an empty queue"

    try:
        q.peek()
        assert False
    except ValueError as e:
        assert str(e) == "Cannot peek at an empty queue"
