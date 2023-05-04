from typing import List

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def kthFromEnd(self, k: int) -> int:
        if k < 0:
            raise ValueError("k must be a positive integer.")
        
        slow = self.head
        fast = self.head
        for i in range(k):
            if fast is None:
                raise ValueError("k is greater than the length of the linked list.")
            fast = fast.next_node
        
        if fast is None:
            raise ValueError("k is equal to the length of the linked list.")
        
        while fast.next_node is not None:
            slow = slow.next_node
            fast = fast.next_node
        
        return slow.value
    
    def insert(self, value):
        node = Node(value)
        node.next_node = self.head
        self.head = node
    
    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next_node
        return False
    
    def __str__(self):
        current = self.head
        output = ''
        while current:
            output += f'{{ {str(current.value)} }} -> '
            current = current.next_node
        return output + 'NULL'
