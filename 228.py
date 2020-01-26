from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i, j = 0, 0
        while j < len(nums):
            if j + 1 < len(nums) and nums[j + 1] - nums[j] == 1: j += 1
            else:
                if j == i: res.append(str(nums[i]))
                else: res.append(str(nums[i]) + "->" + str(nums[j]))
                j += 1
                i = j
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.summaryRanges([0,1,2,4,5,7]))