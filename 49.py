# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]):# -> List[List[str]]:
        strDict = {}
        res = []
        for _str in strs:
            str1 = list(_str)
            str1.sort()
            str2 = ''.join(str1)
            strDict.setdefault(str2, []).append(_str)
        for key in strDict.keys():
            res.append(strDict.get(key))
        return res

if __name__ == '__main__':
    strs = ['eat', 'ate', 'tea', 'tan', 'nat']
    solution = Solution()
    res = solution.groupAnagrams(strs)
    print(res)