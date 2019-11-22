class Solution:
    def toGoatLatin(self, S: str) -> str:
        res = []
        s = S.split(" ")
        for i in range(len(s)):
            if s[i][0] in ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u"):
                res.append(s[i] + "ma" + "a" * (i + 1))
            else:
                res.append(s[i][1:] + s[i][0] + "ma" + "a" * (i + 1))
        return " ".join(res)