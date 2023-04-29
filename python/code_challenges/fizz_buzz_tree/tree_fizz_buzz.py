from typing import List


class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children else []


def fizz_buzz_tree(root: TreeNode) -> TreeNode:
    def fizz_buzz_helper(node: TreeNode) -> TreeNode:
        if not node:
            return None

        new_val = ""
        if node.val % 3 == 0:
            new_val += "Fizz"
        if node.val % 5 == 0:
            new_val += "Buzz"
        if not new_val:
            new_val = str(node.val)

        new_node = TreeNode(new_val)
        for child in node.children:
            new_node.children.append(fizz_buzz_helper(child))

        return new_node

    return fizz_buzz_helper(root)
