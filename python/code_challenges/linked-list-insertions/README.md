
# README.md

## linked-list-insertions

This challenge involves adding three methods - append, insert_before, and insert_after - to an existing implementation of a linked list data structure.

## Whiteboard Process

- ![challenge 6 whiteboard](code_challenge_6_whiteboard.png)

## Approach & Efficiency

- For append, we create a new node with the given value and add it to the end of the linked list. If the list is empty, the new node becomes the head of the list. This algorithm has a time complexity of O(n) since we need to traverse the list to reach the end.
For insert_before, we create a new node with the given value and insert it immediately before the first node that has the specified value. If the list is empty, we raise an exception. If the value to insert before is the head of the list, the new node becomes the new head of the list. Otherwise, we traverse the list until we find the node with the value to insert before or reach the end of the list. If the node is not found, we raise an exception. Once we find the node, we insert the new node before it. This algorithm also has a time complexity of O(n) since we need to traverse the list to find the node.
For insert_after, we create a new node with the given value and insert it immediately after the first node that has the specified value. If the list is empty, we raise an exception. We then traverse the list until we find the node with the specified value or reach the end of the list. If the node is not found, we raise an exception. Once we find the node, we insert the new node after it. This algorithm also has a time complexity of O(n) since we need to traverse the list to find the node.

## Big O

- The time complexity of the insert before and insert after functions is O(n) because we have to traverse through the linked list until the given value is found, which could take up to n steps. The time complexity of the append function is O(1) because we can directly add a new node to the end of the linked list without having to traverse through it

## Solution

- [linked-list-insertions](linked_list_insertions.py)

- [linked-list-insertions](linked_list/linked-list-insertions/README.md)
