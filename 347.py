from typing import List
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict(Counter(nums))
        queue = []
        heapq.heapify(queue)

        for num in hashmap:
            if len(queue) == k:
                if hashmap[num] > queue[0][0]:
                    heapq.heappop(queue)
                    heapq.heappush(queue, (hashmap[num], num))
            elif len(queue) < k:
                heapq.heappush(queue, (hashmap[num], num))

        res = []
        while queue:
            tempValue, tempKey = heapq.heappop(queue)
            res.append(tempKey)
        return res
