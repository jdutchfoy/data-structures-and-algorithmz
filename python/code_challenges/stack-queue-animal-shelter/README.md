# README.md

## stack-queue-animal-shelter

- The goal of this program is to implement an animal shelter that can handle the adoption of dogs and cats. The shelter can store incoming animals and retrieve them based on the adopter's preference.

## Whiteboard Process

- ![white board](Code_Challenge_12_whiteboard.png)

## Approach & Efficiency

- The AnimalShelter class has separate lists to store dogs and cats. The enqueue method stores animals in the corresponding list based on their type. The dequeue method retrieves the animal based on the adopter's preference or returns the animal that has been waiting the longest. If there are no animals or the preference is not valid, an instance of Animal with an empty name is returned.

- Both enqueue and dequeue methods have a time complexity of O(1) as they involve only appending or popping elements from a list. The space complexity is also O(1) as we are only storing references to Animal objects in two separate lists.

## Big O

- enqueue(value): O(1)
- dequeue(): O(1)

## Solution

- [Code Challenge 12 readme](https://github.com/jdutchfoy/data-structures-and-algorithms/blob/main/python/code_challenges/stack-queue-animal-shelter/README.md)
