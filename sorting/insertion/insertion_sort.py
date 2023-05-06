def insertion_sort(arr):
    # loop through each element in the array starting at index 1
    for i in range(1, len(arr)):
        # save the current value to a variable
        value = arr[i]
        # set the comparison index to the previous element
        j = i - 1
        # loop backwards through the sorted portion of the array
        while j >= 0 and arr[j] > value:
            # shift elements to the right until the correct position is found
            arr[j + 1] = arr[j]
            # move the comparison index down one
            j -= 1
        # insert the value into its correct position
        arr[j + 1] = value
    # return the sorted array
    return arr
