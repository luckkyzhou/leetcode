# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def hammingWeight(self, n):
        res = 0

        while n:
            m = n & 1
            res += m
            n = n >> 1
        return res