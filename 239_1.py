from typing import List
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if nums == []: return []
        queue = []
        res = []
        for i in range(len(nums)):
            if queue and queue[0] == i - k:
                queue.pop(0)
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            res.append(nums[queue[0]])
        for i in range(k - 1):
            res.pop(0)
        return res



if __name__ == '__main__':
    solution = Solution()
    res = solution.maxSlidingWindow([1,3,1,2,0,5],3)
    print(res)