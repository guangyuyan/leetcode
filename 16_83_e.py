class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp=ListNode(0)
        tmp.next=head
        while head:
            while head.next and head.next.val==head.val:
                head.next=head.next.next
            head=head.next
        return tmp.next