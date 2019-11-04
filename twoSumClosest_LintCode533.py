class Solution:
    def twoSumCloset (self, nums, target):
        nums.sort()
        i = 0
        j = len(nums) - 1
        diff = 2 ** 31
        while i < j:
            if nums[i] + nums[j] < target:
                if diff > target - nums[i] - nums[j]:
                    res = [nums[i], nums[j]]
                    diff = target - nums[i] - nums[j]
                i += 1
            else:
                j -= 1
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.twoSumCloset([-1, 2, 1, -4], 4)
    print(res)