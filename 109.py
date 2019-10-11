# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        cur = []
        while head:
            cur.append(head.val)
            head = head.next
        return self.sortedList(cur)

    def sortedList(self, cur: list) -> TreeNode:
        if cur == []:
            return None
        else:
            mid = len(cur) // 2
            root = TreeNode(cur[mid])
            root.left = self.sortedList(cur[:mid])
            root.right = self.sortedList(cur[mid + 1:])
        return root