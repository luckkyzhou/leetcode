# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def hammingWeight(self, n):
        ans = 0

        while n:
            m = n & 1
            ans += m
            n = n >> 1
        return ans