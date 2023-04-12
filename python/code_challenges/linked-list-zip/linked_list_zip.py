class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def zip_lists(self, other):
        """Zip two linked lists together into one."""
        if not self.head:
            return other
        if not other.head:
            return self

        current_self = self.head
        current_other = other.head

        while current_self and current_other:
            # Save next nodes before rewiring
            next_self = current_self.next_node
            next_other = current_other.next_node

            # Rewire current nodes
            current_self.next_node = current_other
            current_other.next_node = next_self

            # Move to next nodes
            current_self = next_self
            current_other = next_other

        return self

    def __str__(self):
        """Return a string representation of the linked list."""
        output = ''
        current = self.head
        while current:
            output += f'{{ {str(current.value)} }} -> '
            current = current.next_node
        return output + 'NULL'
