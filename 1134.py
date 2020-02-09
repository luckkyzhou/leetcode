class Solution:
    def isArmstrong(self, N: int) -> bool:
        k = len(str(N))
        res = 0
        for i in str(N):
            res += int(i) ** k
        return res == N