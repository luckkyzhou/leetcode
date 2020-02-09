from typing import List
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        hash2 = set()
        hash3 = set()
        for i in range(len(arr2)):
            hash2.add(arr2[i])
            hash3.add(arr3[i])
        res = []
        for i in range(len(arr1)):
            if arr1[i] in hash2 and arr1[i] in hash3: res.append(arr1[i])
        return res