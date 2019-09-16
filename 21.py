# -*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        x = []
        y = []
        res = ListNode(0)
        cur = res
        while l1:
            x.append(l1.val)
            l1 = l1.next
        while l2:
            y.append(l2.val)
            l2 = l2.next
        x.extend(y)
        x.sort()
        for i in range(len(x)):
            cur.next = ListNode(x[i])
            cur = cur.next
        return res.next