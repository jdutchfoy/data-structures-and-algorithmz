# README.md

## stack-queue-pseudo

- Create a PseudoQueue class that implements a standard queue interface using two Stack instances to create and manage the queue. The PseudoQueue should have the following methods:

enqueue(value): Inserts a value into the PseudoQueue, using a first-in, first-out approach.
dequeue(): Extracts a value from the PseudoQueue, using a first-in, first-out approach.

## Whiteboard Process

- code_challenge_11_whiteboard.png

## Approach & Efficiency

- The PseudoQueue implementation uses two Stack instances to insert and remove values, with the first Stack holding the inserted values and the second Stack holding the removed values. When the second Stack is empty, the values from the first Stack are popped and pushed onto the second Stack to reverse their order, so that a first-in, first-out approach is implemented.

- Both the enqueue and dequeue methods have a time complexity of O(1) because we only use push and pop operations on the stacks. The space complexity is also O(1) since we only use the two stacks, which are created during the initialization of the PseudoQueue.

## Big O

- enqueue(value): O(1)
- dequeue(): O(1)

## Solution

- [Code_Challenge_11_readme](https://github.com/jdutchfoy/data-structures-and-algorithms/blob/main/python/code_challenges/stack-queue-pseudo/README.md)
