# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        hashmap = {}
        res = []

        for index, num in enumerate(nums):
            hashmap[num] = index
        for i, num in enumerate(nums):
            j = hashmap.get(num + k)
            if j is not None:
                res.append(j)
        res = list(set(res))
        return len(res)