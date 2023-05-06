def test_zip_lists():
    # Happy Path: Expected outcome
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(2)

    list2 = LinkedList()
    list2.append(5)
    list2.append(9)
    list2.append(4)

    result = zip_lists(list1.head, list2.head)
    assert str(result) == "1 -> 5 -> 3 -> 9 -> 2 -> 4 -> None"

    # Expected failure
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)

    list2 = LinkedList()
    list2.append(5)
    list2.append(9)
    list2.append(4)

    result = zip_lists(list1.head, list2.head)
    assert str(result) != "1 -> 5 -> 3 -> 9 -> 4 -> None"

    # Edge Case (empty lists)
    list1 = LinkedList()
    list2 = LinkedList()

    result = zip_lists(list1.head, list2.head)
    assert str(result) == "None"

    # Edge Case (one empty list)
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(2)

    list2 = LinkedList()

    result = zip_lists(list1.head, list2.head)
    assert str(result) == "1 -> 3 -> 2 -> None"
