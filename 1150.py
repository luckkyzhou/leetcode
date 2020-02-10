from typing import List
from collections import Counter
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        num = Counter(nums)
        if target in num and num[target] > len(nums) / 2: return True
        else: return False