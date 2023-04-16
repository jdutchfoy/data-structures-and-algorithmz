def zip_lists(list1, list2):
    head = None
    tail = None
    
    while list1 and list2:
        if not head:
            head = list1
            tail = head
            list1 = list1.next
        else:
            tail.next = list2
            tail = tail.next
            list2 = list2.next
        
        if list1:
            tail.next = list1
            tail = tail.next
            list1 = list1.next
    
    if list1:
        if tail:
            tail.next = list1
        else:
            head = list1
    
    if list2:
        if tail:
            tail.next = list2
        else:
            head = list2
    
    return head
