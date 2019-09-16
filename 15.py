# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            # 此if增加了边界条件防止产生重复解
            if i == 0 or nums[i] > nums[i - 1]:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    if s < 0:
                        l += 1
                    elif s > 0:
                        r -= 1
                    elif s == 0:
                        result.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
        return result