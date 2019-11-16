from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def check(s: str) -> bool:
            count = 0
            for char in s:
                if char == "(": count += 1
                elif char == ")":
                    count -= 1
                    if count < 0: return False
            return count == 0

        res = []
        def DFS(s: str, start: int, leftParentheses: int, rightParentheses: int):
            if leftParentheses == 0 and rightParentheses == 0 and check(s):
                res.append(s)
            for i in range(start, len(s)):
                # 如果连续两个括号是一样的，那么就跳过，因为会得到重复的结果
                if i > start and s[i] == s[i - 1]: continue
                if leftParentheses > 0 and s[i] == "(":
                    DFS(s[:i] + s[i + 1:], i, leftParentheses - 1, rightParentheses)
                if rightParentheses > 0 and s[i] == ")":
                    DFS(s[:i] + s[i + 1:], i, leftParentheses, rightParentheses - 1)

        leftParentheses = 0
        rightParentheses = 0
        for char in s:
            if char == "(": leftParentheses += 1
            elif char == ")":
                if leftParentheses > 0: leftParentheses -= 1
                else: rightParentheses += 1
        DFS(s, 0, leftParentheses, rightParentheses)
        return res