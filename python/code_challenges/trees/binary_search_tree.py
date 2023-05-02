import os
import sys
from typing import Union

from binary_tree import BinaryTree, Node

sys.path.insert(0, os.path.abspath(os.path.join('..', os.path.dirname(__file__))))


class BinarySearchTree(BinaryTree):
    def __init__(self, root=None):
        super().__init__(root)

    def add(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left_child is None:
                        current.left_child = new_node
                        break
                    else:
                        current = current.left_child
                elif value > current.value:
                    if current.right_child is None:
                        current.right_child = new_node
                        break
                    else:
                        current = current.right_child

    def contains(self, value: Union[int, float]) -> bool:
        current = self.root

        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left_child
            else:
                current = current.right_child

        return False


def main():
    # Add your code here to test BinarySearchTree
    pass


if __name__ == '__main__':
    main()
