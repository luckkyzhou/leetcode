from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i -= 1
        if i == 0:
            nums.reverse()
            return

        j = i
        while j < len(nums):
            if nums[j] <= nums[i - 1]:
                nums[j - 1], nums[i - 1] = nums[i - 1], nums[j - 1]
                break
            j += 1
        if j == len(nums):
            nums[j - 1], nums[i - 1] = nums[i - 1], nums[j - 1]

        left = i
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        print(nums)
if __name__ == '__main__':
    solution = Solution()
    solution.nextPermutation([1,5,8,4,7,6,5,3,1])
