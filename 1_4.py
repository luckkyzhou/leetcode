class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for idx, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [hashmap[target - num], idx]
            hashmap[num] = idx
