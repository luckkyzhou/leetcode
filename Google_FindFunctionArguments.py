# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def findArguments(self, f, z):
        def binSearch(x, y):
            left = 1
            right = y - 1
            while left <= right:
                mid = (left + right) // 2
                if f(x, mid) == z:  return mid
                elif f(x, mid) < z: left = mid + 1
                else: right = mid - 1
            return -1

        x = 1
        y = 2 ** 32 - 1
        res = []
        while f(x, 1) <= z:
            y = binSearch(x, y)
            if y != -1: res.append([x, y])
            else: y = 2 ** 32 - 1
            x += 1
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.findArguments(lambda x, y: x + 5 * y, 17)
    print(res)