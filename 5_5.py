class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(p, left, right):
            while left >= 0 and right < len(p) and p[left] == p[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        res = ""
        for i in range(len(s)):
            left1, right1 = expand(s, i, i)
            left2, right2 = expand(s, i, i+1)
            if right1 - left1 > len(res):
                res = s[left1:right1+1]
            if right2 - left2 > len(res):
                res = s[left2:right2+1]
        return res