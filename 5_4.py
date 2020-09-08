class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = ""
        for l in range(1, n + 1):
            for i in range(n):
                j = i + l - 1
                if j >= n: break
                if l == 1:
                    dp[i][j] = True
                elif l == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                if dp[i][j] and l > len(res):
                    res = s[i:j+1]
        return res