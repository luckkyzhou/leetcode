from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {}
        hashmap[0] = 1
        res, sum = 0, 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in hashmap:
                res += hashmap[sum - k]
            hashmap[sum] = hashmap.get(sum, 0) + 1
        return res