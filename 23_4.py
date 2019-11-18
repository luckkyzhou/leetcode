import heapq
from typing import List
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        queue = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(queue, (lists[i].val, i))
                lists[i] = lists[i].next

        res = ListNode(0)
        cur = res
        while queue:
            value, index = heapq.heappop(queue)
            cur.next = ListNode(value)
            cur = cur.next
            if lists[index]:
                heapq.heappush(queue, (lists[index].val, index))
                lists[index] = lists[index].next
        return res.next