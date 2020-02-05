class Solution:
    def backspaceCompare(self, S: str, T: str):
        stack_S = []
        stack_T = []

        for s in S:
            if s == "#" and stack_S != []: stack_S.pop()
            elif s != "#": stack_S.append(s)
        for t in T:
            if t == "#" and stack_T != []: stack_T.pop()
            elif t != "#": stack_T.append(t)
        return stack_S == stack_T

if __name__ == '__main__':
    solution = Solution()
    res = solution.backspaceCompare("y#fo##f", "y#f#o##f")
    print(res)