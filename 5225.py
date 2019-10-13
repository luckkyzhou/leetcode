# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1, -1, -1):
            #nums_x = [x for x in nums if x != nums[i]]
            #if len(nums_x) == 0:
            #    return i

            '''for j in range(0, len(nums_x)):
                nums_y = []
                for y in range(j):
                    nums_y.append(nums_x[y])
                for y in range(j + 1, len(nums_x)):
                    nums_y.append(nums_x[y])'''
            nums_x = nums[0:i + 1]
            hashmap = {}
            for key in nums_x:
                hashmap[key] = hashmap.get(key, 0) + 1
            if len(hashmap) == 1:
                return i + 1
            #check = set(list(hashmap.values()))
            #if len(check) == 1:
            #    if 1 in check:
            #        return i + 1
            #if len(check) == 2:
            another = {}
            for k, v in hashmap.items():
                another.setdefault(v, []).append(k)
            if len(another) == 1 and 1 in another.keys():
                return i + 1
            if len(another) == 2 and 1 in another.keys() and len(another[1]) == 1:
                return i + 1
            if len(another) == 2:
                minKey = min(another.keys(), key=(lambda x: x))
                if minKey + 1 in another.keys() and len(another[minKey + 1]) == 1:
                    return i + 1




if __name__ == '__main__':
    solution = Solution()
    nums = [10,2,8,9,3,8,1,5,2,3,7,6]
    res = solution.maxEqualFreq(nums)
    print(res)
