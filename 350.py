from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = set(nums1) & set(nums2)
        res = []
        for i in inter:
            res += [i] * min(nums1.count(i), nums2.count(i))
        return res