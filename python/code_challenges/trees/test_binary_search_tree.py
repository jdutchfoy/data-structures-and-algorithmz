import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join('..', os.path.dirname(__file__))))

from binary_tree import Node
from binary_search_tree import BinarySearchTree


def test_empty_tree():
    tree = BinarySearchTree()
    assert tree.root is None


def test_single_node_tree():
    tree = BinarySearchTree(Node(1))
    assert tree.root.value == 1


def test_add_to_binary_search_tree():
    tree = BinarySearchTree(Node(5))
    tree.add(3)
    tree.add(7)
    assert tree.root
