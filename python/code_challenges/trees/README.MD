# README.md

## tree-max

Write the following method for the Binary Tree class

find maximum value
Arguments: none
Returns: number
Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Whiteboard Process

![challenge 16 whiteboard](code_challenge_16_whiteboard.png)

## Approach & Efficiency

## Big O

## Solution

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self, root):
        self.root = BinaryTreeNode(root)
    def find_max_value(self):
        if self.root is None:
            return None
        max_val = self.root.data
        queue = [self.root]
        while len(queue) > 0:
            node = queue.pop(0)
            if node.data > max_val:
                max_val = node.data
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return max_val

## Test cases

- print(example.find_max_value())

[tree-max](tree-max/tree-max/README.md)
