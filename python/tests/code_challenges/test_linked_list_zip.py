from data_structures.linked_list import LinkedList
from linked_list_zip import zip_lists
import pytest


def test_exists():
    assert zip_lists


def test_zip_lists():
    # Happy Path: Expected outcome
    list1 = LinkedList()
    list1.insert(3)
    list1.insert(2)
    list1.insert(1)

    list2 = LinkedList()
    list2.insert("c")
    list2.insert("b")
    list2.insert("a")

    actual = zip_lists(list1, list2)
    expected = "1 -> a -> 2 -> b -> 3 -> c -> NULL"

    assert str(actual) == expected


def test_even_length():
    list_a = LinkedList()
    for value in reversed([1, 2, 3]):
        list_a.insert(value)

    list_b = LinkedList()
    for value in reversed(["a", "b", "c"]):
        list_b.insert(value)

    actual = zip_lists(list_a, list_b)
    expected = "1 -> a -> 2 -> b -> 3 -> c -> NULL"

    assert str(actual) == expected


def test_a_shorter():
    list_a = LinkedList()
    for value in reversed([1, 2]):
        list_a.insert(value)

    list_b = LinkedList()
    for value in reversed(["a", "b", "c"]):
        list_b.insert(value)

    actual = zip_lists(list_a, list_b)
    expected = "1 -> a -> 2 -> b"

