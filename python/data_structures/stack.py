# Define the Stack class
class Stack:
    """
    A stack is a collection of elements that supports adding elements to the top 
    and removing elements from the top, using a Last-In-First-Out (LIFO) order.
    """

    # Constructor initialize an empty stack
    def __init__(self):
        self.items = []

    # Method add a new element to the top of the stack
    def push(self, item):
        self.items.append(item)

    # Method remove and return the element at the top of the stack
    def pop(self):
        # If the stack is empty, raise an error
        if self.is_empty():
            raise ValueError("Cannot pop from an empty stack")
        else:
            # Otherwise, remove and return the element at the top of the stack
            return self.items.pop()

    # Method return the value of the element at the top of the stack without removing it
    def peek(self):
        # If the stack is empty, raise an error
        if self.is_empty():
            raise ValueError("Cannot peek at an empty stack")
        else:
            # Otherwise, return the value of the element at the top of the stack
            return self.items[-1]

    # Method check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0


# Test the Stack class
def test_stack():
    # Create an empty stack
    s = Stack()

    # Test pushing onto a stack
    s.push(1)
    assert s.items == [1]

    # Test pushing multiple values onto a stack
    s.push(2)
    s.push(3)
    assert s.items == [1, 2, 3]

    # Test popping off the stack
    assert s.pop() == 3
    assert s.items == [1, 2]

    # Test emptying a stack after multiple pops
    s.pop()
    s.pop()
    assert s.is_empty() == True

    # Test peeking the next item on the stack
    s.push(4)
    s.push(5)
    assert s.peek() == 5

   