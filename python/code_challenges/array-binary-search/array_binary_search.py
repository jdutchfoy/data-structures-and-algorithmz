# Helper function that calculates the midpoint of a given range
def calculate_midpoint(left, right):
    return (left + right) // 2

# Helper function that checks if a given value is smaller than the midpoint
def is_smaller(value, midpoint):
    return value < midpoint

# Helper function that checks if a given value is larger than the midpoint
def is_larger(value, midpoint):
    return value > midpoint

# Helper function that updates the search range based on the comparison result
def update_range(value, midpoint, left, right):
    # If the value is smaller than the midpoint, update the right boundary
    if is_smaller(value, midpoint):
        return left, midpoint - 1
    # If the value is larger than the midpoint, update the left boundary
    elif is_larger(value, midpoint):
        return midpoint + 1, right
    # If the value is equal to the midpoint, we've found the key
    else:
        return midpoint, midpoint

# Main function that performs binary search on a sorted array
def binary_search(arr, key):
    # Set the initial search range to the entire array
    left, right = 0, len(arr) - 1

    # Keep searching until the left boundary crosses the right boundary
    while left <= right:
        # Calculate the midpoint of the current search range
        midpoint = calculate_midpoint(left, right)

        # If we found the key, return its index
        if arr[midpoint] == key:
            return midpoint
        # Otherwise, update the search range based on the comparison result
        else:
            left, right = update_range(key, arr[midpoint], left, right)

    # If the key was not found, return -1
    return -1
