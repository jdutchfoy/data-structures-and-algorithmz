# README.md

# Hashtable

## Summary
- This challenge involves implementing a hashtable data structure in Python.

- A hashtable is a data structure that stores key-value pairs and allows for efficient lookup, insertion, and deletion of entries. The goal of this challenge is to implement a hashtable class in Python and write tests to ensure that it works correctly.

## Whiteboard
- The whiteboard image for this challenge can be found [here](./assets/whiteboard.png).


## Approach and Efficiency
- The hashtable is implemented using an array of linked lists, where each index in the array represents a bucket that contains a linked list of key-value pairs. The time complexity of the `set`, `get`, and `has` methods is O(1) on average, but in the worst case, the time complexity can be O(n) if there are many collisions. The space complexity is O(n), where n is the number of entries in the hashtable.

## Code
- The code for this challenge can be found [hastable](hashtable.py).

## Tests
- The tests for this challenge can be found [test](tests/test_hashtable.py).
- The tests for this challenge can be found [test](tests/test_set_and_get.py).

## Big O
- The time complexity of the `set`, `get`, and `has` methods is O(1) on average, but in the worst case, the time complexity can be O(n) if there are many collisions. The space complexity is O(n), where n is the number of entries in the hashtable.

### `set` method
- Time: O(1) on average, O(n) in worst case
- Space: O(1)

### `get` method
- Time: O(1) on average, O(n) in worst case
- Space: O(1)

### `has` method
- Time: O(1) on average, O(n) in worst case
- Space: O(1)

## Checklist
- [ ] Update top-level README file
- [x ] Ensure that the README for the challenge is complete
- [x ] Write unit tests and ensure they are passing
- [ x] Run "Happy Path", "Expected Failure", and "Edge Case" tests
- [ x] Check for code efficiency and complexity
- [x ] Add comments to the code to explain complex sections or functions


- [README](README.md)
