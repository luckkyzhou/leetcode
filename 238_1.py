from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        left = 1
        for i in range(len(nums)):
            res.append(left)
            left *= nums[i]
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res