# -*- coding: utf-8 -*-

from typing import List

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def mergeTwoKLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoKLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoKLists(l1, l2.next)
            return l2

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists.length == 0:
            return []
        if lists.length == 1:
            return lists[0]
        if lists.length == 2:
            return self.mergeTwoKLists(lists[0], lists[1])

        n = len(lists)
        mid = len(lists) // 2
        l1 = []
        l2 = []
        for i in range(mid):
            l1[i] = lists[i]
        for i in range((n - mid), n):
            l2[i] = lists[i]

        return self.mergeTwoKLists(l1, l2)