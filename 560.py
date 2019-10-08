# -*- coding: utf-8 -*-
from typing import List
# 错误解法
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0: return 0

        count = 0
        queue = []
        for i in range(len(nums)):
            queue.append(nums[i])
            if sum(queue) == k:
                count += 1
                queue.pop(0)
            elif sum(queue) > k:
                queue.pop(0)
        if sum(queue) == k and len(queue) > 0:
            count += 1
        if sum(queue) < 0:
            for i in range(len(queue)):
                queue.pop(0)
                if sum(queue) == k:
                    count += 1
                    break
        return count

if __name__ == '__main__':
    solution = Solution()
    input = [-1, -1, 1]
    res = solution.subarraySum(input, 0)
    print(res)