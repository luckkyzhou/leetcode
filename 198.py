from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax = 0
        curMax = 0
        for num in nums:
            temp = curMax
            curMax = max(prevMax + num, curMax)
            prevMax = temp
        return curMax
