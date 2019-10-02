# -*- coding: utf-8 -*-
from string import ascii_lowercase

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        duplicates = [k * ch for ch in ascii_lowercase]

        prev_length = -1
        while prev_length != len(s):
            prev_length = len(s)
            for duplicate in duplicates:
                s = s.replace(duplicate, '')

        return s

if __name__ == '__main__':
    solution = Solution()
    s = 'abbbaad'
    k = 3
    res = solution.removeDuplicates(s, k)
    print(res)