from typing import List

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if len(nums) == 0: return False
        sideSum = sum(num for num in nums)
        if sideSum / 4 * 4 != sideSum: return False
        return self.DFS(nums, 0, len(nums), 0, 0, 0, 0, sideSum / 4)

    def DFS(self, nums: List[int], i: int, length, s1, s2, s3, s4, side) -> bool:
        if i == length:
            if s1 == s2 == s3 == s4 == side: return True
            else: return False
        if s1 > side or s2 > side or s3 > side or s4 > side: return False

        return self.DFS(nums, i + 1, length, s1 + nums[i], s2, s3, s4, side) or self.DFS(nums, i + 1, length, s1, s2 + nums[i], s3, s4, side) or self.DFS(nums, i + 1, length, s1, s2, s3 + nums[i], s4, side) or self.DFS(nums, i + 1, length, s1, s2, s3, s4 + nums[i], side)