from typing import List

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        d = nums[0]
        for num in nums:
            d = self.gcd(d, num)
        return d == 1
    def gcd(self, a, b):
        if a % b == 0:
            return b
        else:
            return self.gcd(b, a % b)