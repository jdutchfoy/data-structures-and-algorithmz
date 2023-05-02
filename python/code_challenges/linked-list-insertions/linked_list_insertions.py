class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        if self.head is None:
            raise Exception("Cannot insert before in an empty list")
        elif self.head.value == value:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None and current_node.next.value != value:
                current_node = current_node.next
            if current_node.next is None:
                raise Exception("Value not found in list")
            new_node.next = current_node.next
            current_node.next = new_node

    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        if self.head is None:
            raise Exception("Cannot insert after in an empty list")
        else:
            current_node = self.head
            while current_node is not None and current_node.value != value:
                current_node = current_node.next
            if current_node is None:
                raise Exception("Value not found in list")
            new_node.next = current_node.next
            current_node.next = new_node
