from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums: List[int]) -> int:
        curMax, prevMax = 0, 0
        for num in nums:
            curMax, prevMax = max(prevMax + num, curMax), curMax
        return curMax