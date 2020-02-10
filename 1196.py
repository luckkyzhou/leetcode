from typing import List
class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        res = 0
        tmp = 0
        for i in range(len(arr)):
            tmp += arr[i]
            if tmp > 5000: return res
            else: res += 1
        return res