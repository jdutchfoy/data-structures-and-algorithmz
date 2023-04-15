from typing import List


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class Stack:
    def __init__(self, head=None):
        self.head = head

    def push(self, value):
        node = Node(value)
        node.next_node = self.head
        self.head = node

    def pop(self):
        if not self.head:
            raise ValueError("Cannot pop from an empty stack")
        value = self.head.value
        self.head = self.head.next_node
        return value

    def peek(self):
        if not self.head:
            raise ValueError("Cannot peek an empty stack")
        return self.head.value

    def is_empty(self):
        return not bool(self.head)


class PseudoQueue:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, value):
        self.stack_1.push(value)

    def dequeue(self):
        if self.stack_2.is_empty():
            while not self.stack_1.is_empty():
                self.stack_2.push(self.stack_1.pop())
        return self.stack_2.pop()


def test_pseudo_queue():
    pq = PseudoQueue()
