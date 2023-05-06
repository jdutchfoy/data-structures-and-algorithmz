from merge_sort import merge_sort


def test_merge_sort():
    # Test cases
    assert merge_sort([8, 4, 23, 42, 16, 15]) == [4, 8, 15, 16, 23, 42]
    assert merge_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
    assert merge_sort([1]) == [1]
    assert merge_sort([]) == []

    # Edge cases
    assert merge_sort([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]




    # The
    # merge
    # sort
    # algorithm
    # checks if the
    # list
    # has
    # only
    # one
    # element or less, and if so, it just returns the list.Otherwise, it divides the list in two halves and repeats the merge sort process recursively for each half.Finally, the sorted halves are merged back together using a function that compares the first elements of each half and appends them in the right order to a result list.The process is repeated until all elements are sorted.This helps to sort large lists efficiently and maintain the relative order of equal elements.
