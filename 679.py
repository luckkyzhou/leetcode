# -*- coding: utf-8 -*-
from typing import List
from operator import add, sub, mul, truediv

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0] == 24

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    filterNums = [nums[k] for k in range(len(nums)) if i != k != j]
                    for op in (add, sub, mul, truediv):
                        if (op is add or op is mul) and j > i:
                            continue
                        if op is not truediv or nums[j]:
                            filterNums.append(op(nums[i], nums[j]))
                            if self.judgePoint24(filterNums):
                                return True
                            filterNums.pop()
        return False

if __name__ == '__main__':
    solution = Solution()
    res = solution.judgePoint24([4,1,8,7])
    print(res)