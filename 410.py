from typing import List
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = low + (high - low) // 2

            temp = 0
            count = 1
            for num in nums:
                temp += num
                if temp > mid:
                    temp = num
                    count += 1
            if count > m: low = mid + 1
            else: high = mid
        return low