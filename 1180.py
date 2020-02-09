class Solution:
    def countLetters(self, S: str) -> int:
        res = 0
        j = 0
        while j < len(S):
            tmp = S[j]
            cnt = 0
            while j < len(S) and S[j] == tmp:
                cnt += 1
                j += 1
            res += (1 + cnt) * cnt // 2
        return res