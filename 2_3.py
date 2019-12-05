class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
class Solution:
    def addTwoNumbers(l1: ListNode,l2: ListNode):
        carry = 0
        res = ListNode(0)
        cur = res

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            carry += x + y
            res.next = ListNode(carry % 10)
            carry //= 10
            res = res.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry: res.next = ListNode(carry)
        return cur.next