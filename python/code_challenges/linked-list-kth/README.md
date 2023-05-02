# README.md

## linked-list-kth

- Write the following method for the Linked List class:

kth from end
argument: a number, k, as a parameter.
Return the node’s value that is k places from the tail of the linked list.
You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Whiteboard Process

- ![white board](code_challenge_7_whiteboard.png)

## Approach & Efficiency

- The function BinarySearch takes in two parameters: arr is the sorted array, and key is the value that we want to find.
- We initialize left and right variables to keep track of the boundaries of the search range. We start with left as 0 and right as the index of the last element in the array.
- We enter a while loop that continues until left becomes greater than right. This means that we have searched the entire array without finding the element.
- Inside the loop, we calculate the midpoint index using integer division.
- We compare the value at the midpoint index with the search key. If they are equal, we have found the element, so we return the index.

## Solution

- class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def kthFromEnd(self, k):
        if k < 0:
            raise ValueError("k must be a positive integer.")
        slow = self.head
        fast = self.head
        for i in range(k):
            if fast is None:
                raise ValueError("k is greater than the length of the linked list.")
            fast = fast.next_node
        if fast is None:
            raise ValueError("k is equal to the length of the linked list.")
        while fast.next_node is not None:
            slow = slow.next_node
            fast = fast.next_node
        return slow.value

  #tests empty list 

- def test_kthFromEnd():
    ll = LinkedList()
    with pytest.raises(ValueError):
        ll.kthFromEnd(0)

- [Code Challenge 07 readme](https://github.com/jdutchfoy/data-structures-and-algorithms/blob/main/python/code_challenges/linked-list-kth/README.md)