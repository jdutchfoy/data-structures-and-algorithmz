import pytest
from .tree_fizz_buzz import fizz_buzz_tree, TreeNode


def test_fizz_buzz_tree():
    # Create an example k-ary tree
    root = TreeNode(
        1,
        [
            TreeNode(3, [TreeNode(5), TreeNode(6)]),
            TreeNode(2, [TreeNode(9), TreeNode(10)]),
        ],
    )

    # Apply fizz_buzz_tree function
    new_root = fizz_buzz_tree(root)

    # Verify that the new tree has the same structure, but with modified node values
    assert new_root.val == "1"
    assert len(new_root.children) == 2
    assert new_root.children[0].val == "Fizz"
    assert new_root.children[1].val == "2"
    assert len(new_root.children[0].children) == 2
    assert new_root.children[0].children[0].val == "Buzz"
    assert new_root.children[0].children[1].val == "Fizz"
    assert len(new_root.children[1].children) == 2
    assert new_root.children[1].children[0].val == "Fizz"
    assert new_root.children[1].children[1].val == "Buzz"

    # Verify that the original tree is not modified
    assert root.val == 1
    assert len(root.children) == 2
    assert root.children[0].val == 3
    assert root.children[1].val == 2
    assert len(root.children[0].children) == 2
    assert root.children[0].children[0].val == 5
    assert root.children[0].children[1].val == 6
    assert len(root.children[1].children) == 2
    assert root.children[1].children[0].val == 9
    assert root.children[1].children[1].val == 10
