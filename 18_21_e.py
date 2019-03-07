def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 and l2:
        if l1.val > l2.val:
            head = l2
            l2 = l2.next
        elif l1.val <= l2.val:
            head = l1
            l1 = l1.next
    elif not l1 and not l2:
        return []
    elif not l1 and l2:
        return l2
    elif l1 and not l2:
        return l1

    head_temp = head
    while l1 or l2:
        if l1 and l2:
            if l1.val < l2.val:
                head_temp.next = l1
                l1 = l1.next
                head_temp = head_temp.next

            elif l1.val >= l2.val:
                head_temp.next = l2
                l2 = l2.next
                head_temp = head_temp.next
        elif l1 and not l2:
            head_temp.next = l1
            break

        elif not l1 and l2:
            head_temp.next = l2
            break

    return head