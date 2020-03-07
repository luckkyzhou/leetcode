class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            temp = a ^ b
            b = (a & b) << 1
            a = temp
        return a