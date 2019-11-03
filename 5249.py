class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        visited = [False for _ in range(len(s))]
        S = []
        for i in range(len(s)):
            if s[i] == '(':
                S.append(i)
            elif s[i] == ')':
                if S == []: continue
                visited[i] = True
                visited[S.pop()] = True
        res = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == ')':
                if visited[i]:
                    res.append(s[i])
            else:
                res.append(s[i])
        return "".join(res)