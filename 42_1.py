# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        max_left = [0 for x in range(n)]
        max_right = [0 for x in range(n)]
        max_left[0] = height[0]
        max_right[n - 1] = height[n - 1]

        # 定义状态
        # range(start, stop, step) start默认0, stop是从start到stop但不包括stop
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])

        # 找到状态转移方程
        result = 0
        for i in range(n):
            result += min(max_left[i], max_right[i]) - height[i]
        return result
