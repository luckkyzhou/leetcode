from typing import List
class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        minimum = 2 ** 31
        for a in A: minimum = min(minimum, a)
        res = 0
        while minimum != 0:
            res += minimum % 10
            minimum //= 10
        return 1 if res & 1 == 0 else 0