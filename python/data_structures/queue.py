# Define the Queue class
class Queue:
    """
    A queue is a collection of elements that supports adding elements to the back 
    and removing elements from the front, using a First-In-First-Out (FIFO) order.
    """

    # Constructor initialize an empty queue
    def __init__(self):
        self.items = []

    # Method add a new element to the back of the queue
    def enqueue(self, item):
        self.items.append(item)

    # Method remove and return the element at the front of the queue
    def dequeue(self):
        # If the queue is empty, raise an error
        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty queue")
        else:
            # Otherwise, remove and return the element at the front of the queue
            return self.items.pop(0)

    # Method return the value of the element at the front of the queue without removing it
    def peek(self):
        # If the queue is empty, raise an error
        if self.is_empty():
            raise ValueError("Cannot peek at an empty queue")
        else:
            # Otherwise, return the value of the element at the front of the queue
            return self.items[0]

    # Method check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0
    
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
