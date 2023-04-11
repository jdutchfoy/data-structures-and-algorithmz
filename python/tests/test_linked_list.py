def test_linked_list():
    # Test append method
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(5)
    linked_list.append(3)
    assert str(linked_list) == "1 -> 5 -> 3 -> NULL"
    
    # Test insert_before method
    linked_list.insert_before(5, 2)
    assert str(linked_list) == "1 -> 2 -> 5 -> 3 -> NULL"
    
    # Test insert_before method with value not found
    try:
        linked_list.insert_before(4, 7)
    except Exception as e:
        assert str(e) == "Value not found in list"
    
    # Test insert_before method with empty list
    try:
        empty_list = LinkedList()
        empty_list.insert_before(3, 4)
    except Exception as e:
        assert str(e) == "Cannot insert before in an empty list"
    
    # Test insert_after method
    linked_list.insert_after(5, 5)
    assert str(linked_list) == "1 -> 2 -> 5 -> 5 -> 3 -> NULL"
    
    # Test insert_after method with value not found
    try:
        linked_list.insert_after(4, 7)
    except Exception as e:
        assert str(e) == "Value not found in list"
    
    # Test insert_after method with empty list
    try:
        empty_list = LinkedList()
        empty_list.insert_after(3, 4)
    except Exception as e:
        assert str(e) == "Cannot insert after in an empty list"
