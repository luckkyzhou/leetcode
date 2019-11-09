from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if nums == []: return []
        queue = deque()
        res = []
        for i in range(len(nums)):
            if queue and queue[0] == i - k:
                queue.popleft()
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            res.append(nums[queue[0]])
        for i in range(k - 1):
            res.popleft()
        return res