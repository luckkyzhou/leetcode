class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = S.upper().replace("-", "")[::-1]
        res = ""
        for i in range(len(s)):
            if i % K == 0 and i != 0:
                res = res + "-"
            res = res + s[i]
        return res[::-1]