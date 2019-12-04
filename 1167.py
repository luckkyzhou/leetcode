from typing import List
import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1: return 0
        res = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            i = heapq.heappop(sticks)
            j = heapq.heappop(sticks)
            res += i + j
            if len(sticks) > 0:
                heapq.heappush(sticks, i + j)
        if sticks:
            res += heapq.heappop(sticks)
        return res