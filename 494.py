from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if sum(nums) < S or (sum(nums) + S) % 2 == 1:
            return 0
        positive = (sum(nums) + S) // 2
        dp = [1] + [0 for _ in range(positive)]

        for num in nums:
            for i in range(positive, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[positive]
