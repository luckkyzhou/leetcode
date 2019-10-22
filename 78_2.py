from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recursion(start, cur):
            res.append(cur)
            for i in range(start, len(nums)):
                recursion(i + 1, cur + [nums[i]])
        recursion(0, [])
        return res

