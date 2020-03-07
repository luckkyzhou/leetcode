class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for x in s:
            res *= 26
            res += ord(x) - ord("A") + 1
        return res