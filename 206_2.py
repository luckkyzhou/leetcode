class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        prev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return prev
