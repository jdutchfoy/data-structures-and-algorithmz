import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join('..', os.path.dirname(__file__))))

from binary_tree import BinaryTree, Node


def test_node():
    node = Node(1)
    assert node.value == 1
    assert node.left_child is None
    assert node.right_child is None


def test_binary_tree():
    tree = BinaryTree()
    assert tree.root is None

    root_node = Node(1)
    tree = BinaryTree(root_node)
    assert tree.root.value == 1

    left_node = Node(2)
    root_node.left_child = left_node
    assert tree.root.left_child.value == 2

    right_node = Node(3)
    root_node.right_child = right_node
    assert tree.root.right_child.value == 3

    result = tree.pre_order(tree.root, [])
    assert result == [1, 2, 3]

    result = tree.in_order(tree.root, [])
    assert result == [2, 1, 3]

    result = tree.post_order(tree.root, [])
    assert result == [2, 3, 1]
