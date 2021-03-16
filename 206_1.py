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
        cur = head
        prev = None

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev