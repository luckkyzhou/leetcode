# -*- coding: utf-8 -*-
from typing import List
import sys

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0: return 0
        if dividend == - 2 ** 31 and divisor == -1:
            return 2 ** 31 - 1

        negative = (dividend ^ divisor) < 0
        absDividend = abs(dividend)
        absDivisor = abs(divisor)
        result = 0
        for i in range(31, -1, -1):
            if (absDividend >> i) >= absDivisor:
                result += 1 << i
                absDividend -= absDivisor << i

        return result if negative else -result