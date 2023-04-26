# README.md

## insertion_sort
Insertion sort is a simple algorithm that sorts an array by iterating through its unsorted values and placing each in its proper sorted position within the sorted sublist.


- Pseudocode
````
  Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted
  ````


- Start with an unsorted list of elements.
- Take the second element in the list and compare it to the first element.
- If the second element is smaller than the first, swap their positions.
- Take the third element in the list and compare it to the second element.
- If the third element is smaller than the second, swap their positions.
- If the second element is still smaller than the first, swap their positions.
- Take the fourth element in the list and compare it to the third element.
- If the fourth element is smaller than the third, swap their positions.
- If the third element is smaller than the second, swap their positions.
- If the second element is still smaller than the first, swap their positions.
- Repeat steps 7-10 for all remaining elements in the list.
- The list is now sorted in ascending order.
- If you want to sort in descending order, simply change the comparison operator from '<' to '>'.
- Insertion sort has a time complexity of O(n^2).
- Although not the most efficient sorting algorithm for large lists, insertion sort is a simple and effective method for smaller lists.

## Visualization

````
Iteration 1: [8, 4, 23, 42, 16, 15]
Iteration 2: [4, 8, 23, 42, 16, 15]
Iteration 3: [4, 8, 23, 42, 16, 15]
Iteration 4: [4, 8, 16, 23, 42, 15]
Iteration 5: [4, 8, 15, 16, 23, 42]
````
- No Whiteboard - Required.

## Feature:
Review the pseudocode below, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

Once you are done with your article, code a working, tested implementation of Insertion Sort based on the pseudocode provided.

- Sample Arrays
In your blog article, visually show the output of processing this input array:
[8,4,23,42,16,15]


## Approach & Efficiency
- [insertion_sort.py](/Users/dutchfoy/projects/401-Projects/data-structures-and-algorithms/sorting/insertion/insertion_sort.py)



## Big O

- The time complexity of the insertion sort algorithm is O(n^2). This means that as the input size increases, the number of operations needed to sort the array grows exponentially. The space complexity is O(1), which means that the amount of extra memory needed to sort the array does not increase as the size of the input increases.

## Test
- Virtual environment
- Pytest

- [test_insertion_sort](..%2F..%2F..%2F..%2F..%2FDesktop%2Ftest_insertion_sort.py.png)

