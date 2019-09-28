# -*- coding: utf-8 -*-
from typing import List

'''
the volume = (a[y] - a [x]) * min(height(a[y]), height(a[x]))
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0: return 0
        i = 0
        j = len(height) - 1
        res = 0

        while i < j:
            minHeight = min(height[i], height[j])
            res = max(res, minHeight * (j - i))
            if height[i] < height[j]: i += 1
            else: j -= 1

        return res