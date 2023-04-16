# README.md

## linked-list-zip

- The problem is to write a function that takes in two linked lists and returns a new linked list that is the result of "zipping" the two input lists together. The nodes of the new list should alternate between the nodes of the two input lists, starting with the first node of the first list, then the first node of the second list, then the second node of the first list, and so on.

## Whiteboard Process

- 

## Approach & Efficiency

- This algorithm uses a while loop to iterate through both input lists, adding nodes to the new list one by one. It keeps track of the head and tail of the new list using two variables, and adds any remaining nodes from one of the input lists to the new list at the end.

## Big O

- The time complexity of this algorithm is O(n), where n is the length of the longer input list. This is because we need to iterate through each node of the longer list in order to create the new list. The space complexity of this algorithm is O(1), because we only need to create a few extra variables to keep track of the head and tail of the new list.

## Solution

- [linked-list-zip](linked-list-zip.py)

- [Code Challenge 08 readme](https://github.com/jdutchfoy/data-structures-and-algorithms/blob/main/python/code_challenges/linked-list-zip/README.md)
