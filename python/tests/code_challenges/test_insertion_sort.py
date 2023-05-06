import pytest
from sorting.insertion.insertion_sort import insertion_sort

def test_insertion_sort():
    assert insertion_sort([2, 1, 3]) == [1, 2, 3]  # Three element array
    assert insertion_sort([1, 2, 3]) == [1, 2, 3]  # Three element array (already sorted)
    assert insertion_sort([5, 2, 1, 3, 6, 4]) == [1, 2, 3, 4, 5, 6]  # Six element array
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]  # Five element array (descending order)
    assert insertion_sort([1]) == [1]  # One element array


# The provided test scenarios aim to verify that the insertion sort function correctly sorts different types of input arrays.
#
# The first test scenario tests an array with three elements that are not in sorted order. The expected result is a sorted array with the same three elements.
#
# The second test scenario tests an array with three elements that are already sorted. The expected result is a sorted array with the same three elements, without any changes.
#
# The third test scenario tests an array with six elements that are not in sorted order. The expected result is a sorted array with the same six elements.
#
# The fourth test scenario tests an array with five elements that are in descending order. The expected result is a sorted array with the same five elements in ascending order.
#
# The fifth test scenario tests an array with only one element. The expected result is a sorted array with the same one element, which is already considered sorted.
#
