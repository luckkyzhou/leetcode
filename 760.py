from typing import List
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        hashB = {}
        for idx, num in enumerate(B):
            hashB[num] = idx
        res = []
        for i in range(len(A)):
            res.append(hashB[A[i]])
        return res