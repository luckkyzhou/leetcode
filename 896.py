from typing import List
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        a, b = 0, 0
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]: a = 1
            if A[i] > A[i + 1]: b = 1
        return False if a + b == 2 else True