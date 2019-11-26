from typing import List
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        res = 1
        dp = [{} for i in range(len(A))]

        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                n = dp[j].get(diff, 1) + 1
                dp[i][diff] = n
            res = max(res, max(dp[i].values()))
        return res