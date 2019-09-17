# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        sum = 0

        for i in range(len(nums)):
            if sum > 0:
                sum += nums[i]
            else:
                sum = nums[i]
            res = max(res, sum)
        return res