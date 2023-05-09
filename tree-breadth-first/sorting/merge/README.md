# README.md

## merge_sort

- Merge sort is a recursive algorithm that sorts an array by dividing it into smaller sub-arrays, sorting those sub-arrays, and then merging them back together


- Pseudocode

````
function merge_sort(list)
    if length(list) ≤ 1
        return list

    middle = length(list) / 2
    left = empty list
    right = empty list

    for each element in list up to middle
        add element to left

    for each element in list after middle
        add element to right

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

function merge(left, right)
    result = empty list

    while length(left) > 0 and length(right) > 0
        if first(left) ≤ first(right)
            append first(left) to result
            left = rest(left)
        else
            append first(right) to result
            right = rest(right)

    if length(left) > 0
        append left to result
    if length(right) > 0
        append right to result

    return result
  ````


- Start with an unsorted array: [8, 4, 23, 42, 16, 15]
- Divide the array in half: [8, 4, 23] and [42, 16, 15]
- Divide each half in half again: [8], [4, 23] and [42], [16, 15]
- Merge the two halves of the second level, resulting in [4, 8, 23] and [15, 16, 42]
- Merge the two halves of the first level, resulting in the sorted array [4, 8, 15, 16, 23, 42]
- Start with an unsorted array: [5, 1, 9, 3, 7, 6, 2, 8, 4]
- Divide the array in half: [5, 1, 9, 3, 7] and [6, 2, 8, 4]
- Divide each half in half again: [5, 1], [9, 3, 7] and [6, 2], [8, 4]
- Divide each half in half again: [5], [1], [9], [3, 7] and [6], [2], [8], [4]
- Merge the two halves of the third level, resulting in [1, 5], [3, 7, 9], [2, 6] and [4, 8]
- Merge the two halves of the second level, resulting in [1, 3, 5, 7, 9] and [2, 4, 6, 8]
- Merge the two halves of the first level, resulting in the sorted array [1, 2, 3, 4, 5, 6, 7, 8, 9]

## Visualization

````
Step-by-Step

Step	Array
1	[8, 4, 23, 42, 16, 15]
2	[8, 4, 23] and [42, 16, 15]
3	[8], [4, 23] and [42], [16, 15]
4	[4, 8, 23] and [15, 16, 42]
5	[4, 8, 15, 16, 23, 42]
6	[5, 1, 9, 3, 7, 6, 2, 8, 4]
7	[5, 1, 9, 3, 7] and [6, 2, 8, 4]
8	[5, 1], [9, 3, 7] and [6, 2], [8, 4]
9	[5], [1], [9], `[3
````
- No Whiteboard - Required.

## Feature:

Review the pseudocode above for the merge sort algorithm, which sorts a list of elements by recursively dividing it into smaller sublists, sorting those sublists, and then merging them back together. Trace the algorithm by stepping through the process with a provided sample array, and document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

Once you are done with your article, code a working, tested implementation of merge sort based on the pseudocode provided.


- Sample Arrays
In your blog article, visually show the output of processing this input array:
[8,4,23,42,16,15]


## Approach & Efficiency

- Merge sort is a stable, comparison-based sorting algorithm that recursively divides an array into smaller sub-arrays until they are small enough to be sorted. It then merges the sorted sub-arrays back together to create the final sorted array. It has a worst-case time complexity of O(n log n), making it more efficient than quicksort for large arrays. While it may not be the fastest for small arrays due to its overhead for recursion and copying, it is still a popular choice for sorting large arrays.



## Big O

The time complexity of merge sort is O(n log n), which means that the number of operations needed to sort an array grows in proportion to n times the logarithm of n. Merge sort has a space complexity of O(n), which means that the amount of extra memory needed to sort an array grows in proportion to n.


## Test
- Virtual environment
- Pytest

- [test_merge_sort](python/tests/code_challenges/test_merge_sort.py)

-[Link to readme.me](./readme.me)
