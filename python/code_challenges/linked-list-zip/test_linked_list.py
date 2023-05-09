from data_structures.linked_list import LinkedList
import pytest


def test_insert():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(5)
    linked_list.insert(3)
    assert str(linked_list) == "3 -> 5 -> 1 -> NULL"


def test_append():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(5)
    linked_list.append(3)
    assert str(linked_list) == "1 -> 5 -> 3 -> NULL"


def test_insert_before():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(5)
    linked_list.insert(3)
    linked_list.insert_before(5, 2)
    assert str(linked_list) == "3 -> 2 -> 5 -> 1 -> NULL"


def test_insert_before_empty_list():
    empty_list = LinkedList()
    with pytest.raises(ValueError):
        empty_list.insert_before(3, 4)


def test_insert_before_value_not_found():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(5)
    linked_list.insert(3)
    with pytest.raises(ValueError):
        linked_list.insert_before(4, 7)


def test_insert_after():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(5)
    linked_list.insert(3)
    linked_list.insert_after(5, 2)
    assert str(linked_list) == "3 -> 5 -> 2 -> 1 -> NULL"


def test_insert_after_empty_list():
    empty_list = LinkedList()
    with pytest.raises(ValueError):
        empty_list.insert_after(3, 4)


def test_insert_after_value_not_found():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(5)
    linked_list.insert(3)
    with pytest.raises(ValueError):
        linked_list.insert_after(4, 7)
