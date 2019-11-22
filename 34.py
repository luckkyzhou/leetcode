from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)
        res = []
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        if left == len(nums) or nums[left] != target:
            res += [-1, -1]
            return res
        else:
            res.append(left)

        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        res.append(right - 1)
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.searchRange([5,7,7,8,8,10],8)
    print(res)