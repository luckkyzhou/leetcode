class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        dp = [[False] * len(s) for _ in range(len(s))]
        res = ''

        for l in range(len(s)):
            for i in range(len(s)):
                j = i + l
                if j >= len(s): break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(res):
                    res = s[i:j + 1]
        return res
