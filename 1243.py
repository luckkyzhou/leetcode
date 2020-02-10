from typing import List
import copy
class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        cpy = copy.copy(arr)
        for i in range(1, len(arr) - 1):
            if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]: cpy[i] += 1
            elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]: cpy[i] -= 1
        return cpy if cpy == arr else self.transformArray(cpy)