class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.0
        i = abs(n)
        while i != 0:
            if i % 2 != 0:
                res *= x
            x *= x
            i //= 2
        return 1 / res if n < 0 else res