from typing import List
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(x):
            rotationA, rotationB = 0, 0
            for i in range(len(A)):
                if A[i] != x and B[i] != x: return -1
                elif A[i] != x: rotationA += 1
                elif B[i] != x: rotationB += 1
            return min(rotationA, rotationB)

        rotation = check(A[0])
        if rotation != -1 or A[0] == B[0]: return rotation
        else: return check(B[0])