from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0: return False
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i - 1, -1, -1):

                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True

                    break
        return dp[-1]

if __name__ == '__main__':
    solution = Solution()
    res = solution.wordBreak("aaaaaaa",["aaaa","aaa"])
    print(res)