# README.md

## Binary Search Tree Implementation

- [Whiteboard](./path/to/whiteboard.png)


## Problem Domain

- The problem domain is to create a binary search tree that has a Node class with properties for the value stored in the node, the left child node, and the right child node. The BinaryTree class should define a method for each of the depth-first traversals: pre-order, in-order, and post-order. Each depth-first traversal method should return an array of values, ordered appropriately. The BinarySearchTree class should be a sub-class of the BinaryTree class and have additional methods for adding a new node with a value in the correct location in the binary search tree and checking whether a value is in the tree at least once.

## Input/Output

- The input for this implementation will be a value to add to the binary search tree or a value to search for in the tree. The output will be a boolean indicating whether the value is in the tree or not or a collection of values from a pre-order, in-order, or post-order traversal.
-
           5
         /   \
        3     7
       /       \
      1         9

## Approach & Efficiency

- To implement the binary search tree, I used a node class with properties for the value stored in the node, the left child node, and the right child node. I also used a binary tree class with methods for each of the depth-first traversals: pre-order, in-order, and post-order. Finally, I used a binary search tree class that is a sub-class of the binary tree class with additional methods for adding a new node with a value in the correct location in the binary search tree and checking whether a value is in the tree at least once.

- The time complexity of adding a new node to the binary search tree or searching for a value in the tree is O(log n) in the average case and O(n) in the worst case. The space complexity of the binary search tree is O(n).

## Solution

- [Code](binary_search_tree.py)
- [Code](binary_tree.py)
- [Code](node.py)
- [Tests](test_binary_search_tree.py)
- [Tests](test_tree_classes.py)

![tests pass](..%2F..%2F..%2F..%2F..%2F..%2FDesktop%2Ftests%20pass.png)



- node.py: This file contains the implementation of the Node class.
- binary_tree.py: This file contains the implementation of the BinaryTree class.
- binary_search_tree.py: This file contains the implementation of the BinarySearchTree class.
- test_binary_search_tree.py: This file contains the test cases used to validate the functionality of the implementation.


- **During development, there were some challenges in creating code that passed the tests. In some cases, the tests had to be revised to better align with the problem statement requirements. However, once the tests were appropriately designed, they proved to be a valuable tool in ensuring the correctness of the implementation.**

## Links


- [README](README.MD)
