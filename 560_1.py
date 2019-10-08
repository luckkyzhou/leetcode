# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, sum = 0, 0
        hashmap = {}
        # sum - k = 0
        hashmap[0] = 1
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in hashmap:
                res += hashmap[sum - k]
            if sum not in hashmap:
                hashmap[sum] = 1
            else:
                hashmap[sum] += 1
        return res