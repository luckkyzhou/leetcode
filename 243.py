# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def shortWordDistance(self, words: List[str], w1: str, w2: str) -> int:
        p1 = -1
        p2 = -1
        l = len(words)
        res = 100

        for i in range(l):
            if words[i] == w1:
                p1 = i
            elif words[i] == w2:
                p2 = i

            if p1 != -1 and p2 != -1:
                res = min(res, abs(p1 - p2))
        return res

if __name__ == '__main__':
    solution = Solution()
    words = ['practice', 'makes', 'good', 'coding', 'makes']
    w1 = 'makes'
    w2 = 'coding'
    result = solution.shortWordDistance(words, w1, w2)
    print(result)