class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        linked_list_str = ""
        current = self.head
        while current:
            linked_list_str += str(current.value) + " -> "
            current = current.next_node
        return linked_list_str + "NULL"

    def insert(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next_node
        return False

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = new_node

    def insert_before(self, value, new_value):
        if not self.head:
            raise ValueError("List is empty")
        if self.head.value == value:
            self.insert(new_value)
            return
        current = self.head
        while current.next_node:
            if current.next_node.value == value:
                new_node = Node(new_value, current.next_node)
                current.next_node = new_node
                return
            current = current.next_node
        raise ValueError(f"Value {value} not found")

    def insert_after(self, value, new_value):
        if not self.head:
            raise ValueError("List is empty")
        current = self.head
        while current:
            if current.value == value:
                new_node = Node(new_value, current.next_node)
                current.next_node = new_node
                return
            current = current.next_node
        raise ValueError(f"Value {value} not found")
