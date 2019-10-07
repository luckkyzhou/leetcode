# -*- coding: utf-8 -*-
from typing import List
from collections import Counter

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        count = 0
        hashmap = {}
        if difference == 0:
            res = dict(Counter(arr))
            return len({key:value for key,value in res.items()if value > 1})
        arr1 = list(set(arr))
        if difference > 0:
            arr1.sort()
        else:
            arr1.sort(reverse=True)
        for index, num in enumerate(arr1):
            hashmap[index] = num
        while hashmap:
            for key in list(hashmap.keys()):
                if hashmap[key] + difference in hashmap.values():
                    hashmap[key] = hashmap[key] + difference
                else:
                    del hashmap[key]
            print(hashmap)
            count += 1
        return count

if __name__ == '__main__':
    solution = Solution()
    #res = solution.longestSubsequence([1,5,7,8,5,3,4,2,1] ,-2)
    #res = solution.longestSubsequence([1,2,3,4], 1)
    #res = solution.longestSubsequence([4,12,10,0,-2,7,-8,9,-9,-12,-12,8,8],0)
    res = solution.longestSubsequence([-54,-63,-62,-69,55,48,-67,-94,-46,-48,91,99,-3,77,-85,-52,15,57,-19,46,72,17,78,59,-26,-24,-14,-7,-37,100,-64,-77,-10,-52,68,-60,-16,-58,84,87,-3,11,-26,-62,-37,-14,-21,28,-69,54,35,10,-92,46,-15,88,-20,20,-17,-76,-54,-96,61,3,-52,4,88,-54,66,-96,-31,10,78,44,-6,-34,-97,-72,34,-93,-71,6,17,-100,32,31,-81,53,-9,17,97,44,-83,7,-20,2,73,-2,-81,-50], 14)
    print(res)