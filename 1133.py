from typing import List
from collections import Counter
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        res = -1
        hashmap = Counter(A)
        for key in hashmap:
            if hashmap[key] == 1: res = max(res, key)
        return res