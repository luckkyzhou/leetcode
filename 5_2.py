# -*- coding: utf-8 -*-

class Solution:
    def longestPalindrome(self, s:str) -> str:
        size = len(s)
        # 如果输入字符串长度为1，则直接返回，必为回文
        if size <= 1:
            return s

        # 设定状态：dp为布尔型二维数组
        # 二维数组两个[]，第一个设定列数和内容，第二个设定行数
        dp = [[False for i in range(size)] for i in range(size)]
        # 设定回文字符串搜索长度。设定回文字符串内容。
        longest_str = 1
        res = s[0]

        # 右边界
        for r in range(1,size):
            # 左边界
            for l in range(r):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_str = r - l + 1
                    if cur_str > longest_str:
                        longest_str = cur_str
                        # 要加1，不然输出少一个字符
                        res = s[l:r + 1]
        return res