# -*- coding: utf-8 -*-

class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size <= 1:
            return s
        # 二维dp问题
        # 状态：dp[l,r]:s[l:r] 闭区间包括l,r 表示判断字符串是不是回文串
        dp = [[False for _ in range(size)]for _ in range(size)]

        longest_l = 1
        res = s[0]

        # 右边界从1开始
        for r in range(1, size):
            for l in range(r):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    if cur_len > longest_l:
                        longest_l = cur_len
                        res = s[l:r + 1]
        return res