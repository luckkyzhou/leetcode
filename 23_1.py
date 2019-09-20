# -*- coding: utf-8 -*-

import heapq
from typing import List

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l1 = ListNode(0)
        cur = l1
        head = []

        # 将所有链表的头结点放入堆中
        for i in range(len(lists)):
            if lists[i]:
                # 将指定的值放入堆head中
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next

        while head:
            # 将堆中最小值给pop出来
            val, idx = heapq.heappop(head)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return l1.next

