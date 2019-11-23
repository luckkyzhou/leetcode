class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        lenS = len(s)
        lenT = len(t)

        if lenS > lenT: return self.isOneEditDistance(t, s)
        if lenT - lenS > 1: return False

        for i in range(lenS):
            if s[i] != t[i]:
                if lenS == lenT:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]
        return lenT == lenS + 1

if __name__ == '__main__':
    solution = Solution()
    res = solution.isOneEditDistance("ab", "acb")
    print(res)