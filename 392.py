class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s[i] not in t:
                return False
            else:
                index = t.index(s[i])
                t = t[index + 1:]
        return True