class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        res = ListNode(0)
        cur = res

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            sum = x + y + carry
            res.next = ListNode(sum % 10)
            res = res.next
            carry = sum // 10

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry: res.next = ListNode(carry)
        return cur.next
