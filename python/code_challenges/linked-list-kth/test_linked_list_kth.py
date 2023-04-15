# def test_kthFromEnd_happy_path():

ll = LinkedList()
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
assert ll.kthFromEnd(2) == 4

# def test_kthFromEnd_list_of_size_one():
ll = LinkedList()
ll.insert(5)
assert ll.kthFromEnd(0) == 5

# def test_kthFromEnd_k_is_not_positive():
ll = LinkedList()
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
try:
        ll.kthFromEnd(-1)
except ValueError as e:
        assert str(e) == "k must be a positive integer."

#def test_kthFromEnd_k_is_equal_to_length():
ll = LinkedList()
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
try:
        ll.kthFromEnd(4)
except ValueError as e:
        assert str(e) == "k is equal to the length of the linked list."

# def test_kthFromEnd_k_is_greater_than_length():
ll = LinkedList()
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
try:
        ll.kthFromEnd(5)
except ValueError as e:
        assert str(e) == "k is greater than the length of the linked list."
