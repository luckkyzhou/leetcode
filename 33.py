# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binSearch(nums, 0, len(nums) - 1, target)
    def binSearch(self, nums: List[int], low: int, high: int, target: int) :
        if low > high: return -1
        mid = (low + high) // 2
        if nums[mid] == target: return mid
        if nums[mid] < nums[high]:
            if nums[mid] < target <= nums[high]:
                return self.binSearch(nums, mid + 1, high, target)
            else:
                return self.binSearch(nums, low, mid - 1, target)
        else:
            if nums[low] <= target < nums[mid]:
                return self.binSearch(nums, low, mid - 1, target)
            else:
                return self.binSearch(nums, mid + 1, high, target)
