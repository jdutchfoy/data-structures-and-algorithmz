def reverse_array(arr):
    reversed_list = []
    for index in range(len(arr)-1, -1, -1):
        reversed_list.append(arr[index])
    return reversed_list
