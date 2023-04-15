# linked-list-zip

- We need to write a function that takes two linked lists as input and merges them by alternating nodes between them. The function should return a new linked list and keep extra space to a minimum.

## Whiteboard Process

- <img width="2656" alt="code_challenge_8_whiteboard 2" src="https://user-images.githubusercontent.com/118240863/232258769-742e5da9-6a12-4085-a2f3-6909754c6a9a.png">



## Approach & Efficiency

- First, check if either list is empty. If one list is empty, we can return the other list as it is.
Create a new linked list called "result" that we will use to store the merged nodes.
Initialize two pointers called "current1" and "current2" to the heads of the two input lists.
We then loop through the lists and alternate nodes between them until we reach the end of one list or both lists. To do this, we add the current node from list1 to the end of the result list, then add the current node from list2 to the end of the result list, and finally move both pointers to the next node in their respective lists.
If we reach the end of one list before the other, we add the remaining nodes from the other list to the end of the result list.
Finally, we return the head of the result list.

## Big O

-  algorithm has a time complexity of O(n), where n is the length of the longer of the two input lists. The space complexity is O(1), as we only create a constant number of new nodes.

## Solution

- [code challenge 8](linked_list_zip.py)
