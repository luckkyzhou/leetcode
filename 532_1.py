from typing import List
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0: return 0
        visied = set()
        res = set()
        for num in nums:
            if num - k in visied: res.add(num - k)
            if num + k in visied: res.add(num)
            visied.add(num)
        return len(res)