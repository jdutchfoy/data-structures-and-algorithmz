from data_structures.linked_list import LinkedList


def zip_lists(list1, list2):
    if not list1.head:
        return list2
    if not list2.head:
        return list1
    current1 = list1.head
    current2 = list2.head
    while current1 and current2:
        temp1 = current1.next_node
        temp2 = current2.next_node
        current1.next_node = current2
        current2.next_node = temp1
        current1 = temp1
        current2 = temp2
    return list1
