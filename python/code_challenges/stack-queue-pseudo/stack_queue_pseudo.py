from typing import List


class Node:
    def __init__(self, value: any, next_node=None):
        self.value = value
        self.next_node = next_node


class Stack:
    def __init__(self, head=None):
        self.head = head

    def push(self, value: any):
        node = Node(value)
        node.next_node = self.head
        self.head = node

    def pop(self) -> any:
        if not self.head:
            raise ValueError("Cannot pop from an empty stack")
        value = self.head.value
        self.head = self.head.next_node
        return value

    def peek(self) -> any:
        if not self.head:
            raise ValueError("Cannot peek an empty stack")
        return self.head.value

    def is_empty(self) -> bool:
        return not bool(self.head)


class PseudoQueue:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, value: any):
        self.stack_1.push(value)

    def dequeue(self) -> any:
        if self.stack_2.is_empty():
            while not self.stack_1.is_empty():
                self.stack_2.push(self.stack_1.pop())
        return self.stack_2.pop()


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


if __name__ == "__main__":
    test_pseudo_queue()
