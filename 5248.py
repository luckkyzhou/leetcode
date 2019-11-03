from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        hashmap = {}
        s = 0
        hashmap[s] = 1
        res = 0
        for i in range(len(nums)):
            if nums[i] & 1 == 1:
                s += 1
            if s - k >= 0:
                res += hashmap[s - k]
            if s not in hashmap.keys():
                hashmap[s] = 1
            else:
                hashmap[s] += 1
        return res