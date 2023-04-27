# README.md

## stack-queue-brackets

- Given a string containing brackets ({}, [], ()), determine if the string's brackets are balanced.

## Whiteboard Process

- ![alt text](image_file_path.png)

## Approach & Efficiency

- Create an empty stack
- Iterate through each character in the input string
- If character is opening bracket, push onto stack
- If character is closing bracket, pop most recent opening bracket and check for match
- If match, continue iterating
- If no match, return False
- If stack not empty after iterating, return False
- Otherwise, return True
 Time complexity: O(n)
Space complexity: O(n)

## Big O

- The algorithm's time complexity is O(n), where n represents the length of the input string. This is because we traverse through the whole string only once. The space complexity is also O(n), as in the worst-case scenario, we will store all opening brackets on the stack before removing them.

Time: O(n), where n is the length of the longest linked list
Space: O(1)

## Solution

[view code](stack_queue_brackets.py)

![code test result](..%2F..%2F..%2F..%2F..%2F..%2FDesktop%2Fstack_queue_brackets%20test%20proof.png)

[Link to README.md](./README.md)

