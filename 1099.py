from typing import List
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        left = 0
        right = len(A) - 1
        res = -1

        A.sort()
        while left < right:
            if A[left] + A[right] >= K:
                right -= 1
            else:
                res = max(res, A[left] + A[right])
                left += 1
        return res