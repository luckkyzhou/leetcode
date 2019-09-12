# -*- coding: utf-8 -*-

class Solution:
    def longestPalindrome(self, s:str) -> str:
        size = len(s)
        # 如果输入字符串长度为1，则直接返回，必为回文
        if size <= 1:
            return size

        # 设定状态：dp为布尔型二维数组
        # 二维数组两个[]，第一个设定列数和内容，第二个设定行数
        dp = [[False for i in range(size)] for i in range(size)]
        