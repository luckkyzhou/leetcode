from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        res = []
        for i in range(len(nums1)):
            hashmap[nums1[i]] = hashmap.get(nums1[i], 0) + 1
        for i in range(len(nums2)):
            if nums2[i] in hashmap and hashmap[nums2[i]] > 0:
                hashmap[nums2[i]] -= 1
                res.append(nums2[i])
        return res