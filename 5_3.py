# -*- coding: utf-8 -*-

class Solution:
    def longestPalindrome(self, s:str) -> str:
        size = len(s)
        if size <= 1:
            return s

        dp = [[False for i in range(size)] for i in range(size)]
        longest_str = 1
        res = s[0]

        for r in range(1, size):
            for l in range(r):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_str = r - l + 1
                    if cur_str > longest_str:
                        longest_str = cur_str
                        res = s[l:r + 1]
        return res