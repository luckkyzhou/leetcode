# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None

        while head:
            cur = head.next
            head.next = prev
            prev = head
            head = cur

        return prev

if __name__ == '__main__':
    head = ListNode(1)
    cur = head
    head.next = ListNode(2)
    head = head.next
    head.next = ListNode(3)

    solution = Solution()
    res = solution.reverseList(cur)
    while res:
        print(res.val)
        res = res.next