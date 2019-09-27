# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        res = []
        # 存储该数左边的数的乘积
        for i in range(len(nums)):
            res.append(left)
            left *= nums[i]
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
