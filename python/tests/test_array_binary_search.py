def test_calculate_midpoint():
    # Test the midpoint calculation with an even-sized range
    assert calculate_midpoint(0, 2) == 1

    # Test the midpoint calculation with an odd-sized range
    assert calculate_midpoint(0, 3) == 1

def test_is_smaller():
    # Test the is_smaller function when the value is smaller than the midpoint
    assert is_smaller(1, 2) == True

    # Test the is_smaller function when the value is equal to the midpoint
    assert is_smaller(2, 2) == False

    # Test the is_smaller function when the value is larger than the midpoint
    assert is_smaller(3, 2) == False

def test_is_larger():
    # Test the is_larger function when the value is smaller than the midpoint
    assert is_larger(1, 2) == False

    # Test the is_larger function when the value is equal to the midpoint
    assert is_larger(2, 2) == False

    # Test the is_larger function when the value is larger than the midpoint
    assert is_larger(3, 2) == True

def test_update_range():
    # Test the update_range function when the value is smaller than the midpoint
    assert update_range(1, 2, 0, 4) == (0, 1)

    # Test the update_range function when the value is equal to the midpoint
    assert update_range(2, 2, 0, 4) == (2, 2)

    # Test the update_range function when the value is larger than the midpoint
    assert update_range(3, 2, 0, 4) == (3, 4)

def test_binary_search():
    # Test binary search with a valid key that is in the array
    assert binary_search([1, 2, 3, 4, 5], 1) == 0

    # Test binary search with a valid key that is not in the array
    assert binary_search([1, 2, 3, 4, 5], 6) == -1

    # Test binary search with an empty array
    assert binary
