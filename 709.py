class Solution:
    def toLowerCase(self, str: str) -> str:
        res = []
        for s in str:
            res.append(chr(ord(s) | 32))
        return "".join(res)