class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = dict()

        for idx, num in enumerate(nums):
            if target-num in hashmap:
                return [hashmap[target-num], idx]
            hashmap[num] = idx
        return []
