class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        maxLen = len(A + A + B)
        i = 1
        a = A
        while len(a) < maxLen:
            if B in a: return i
            else:
                i += 1
                a += A
        return -1