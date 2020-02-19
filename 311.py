from typing import List
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        rowA = len(A)
        colB = len(B[0])
        res = [[0 for _ in range(colB)] for _ in range(rowA)]

        for idxA, valueA in enumerate(A):
            for idxB, valueB in enumerate(zip(*B)):
                res[idxA][idxB] = sum(i * j for i, j in zip(valueA, valueB))
        return res