from stack import Stack

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