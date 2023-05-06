def test_append():
    linked_list = LinkedList()
    linked_list.append(1)
    assert linked_list.head.value == 1
    linked_list.append(2)
    assert linked_list.head.next.value == 2


def test_insert_before():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(3)
    linked_list.append(2)
    linked_list.insert_before(3, 5)
    assert linked_list.head.next.value == 5
    linked_list.insert_before(1, 5)
    assert linked_list.head.value == 5
    linked_list.insert_before(2, 5)
    assert linked_list.head.next.next.value == 5


def test_insert_after():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(3)
    linked_list.append(2)
    linked_list.insert_after(3, 5)
    assert linked_list.head.next.next.value == 5
    linked_list.insert_after(2, 5)
    assert linked_list.head.next.next.next.value == 5


def test_insert_exception():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(3)
    linked_list.append(2)
    try:
        linked_list.insert_before(4, 5)
    except Exception as e:
        assert str(e) == "Value not found in list"
    try:
        linked_list.insert_after(4, 5)
    except Exception as e:
        assert str(e) == "Value not found in list"
    try:
        empty_list = LinkedList()
        empty_list.insert_before(1, 5)
    except Exception as e:
        assert str(e) == "Cannot insert before in an empty list"
        try:
            empty_list = LinkedList()
            empty_list.insert_after(1, 5)
        except Exception as e:
    assert
