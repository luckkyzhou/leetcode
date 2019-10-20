class Solution:
    def decodeString(self, s: str) -> str:
        s = list(s)
        stack = []
        res = ""
        multiple = ""
        while s:
            c = s.pop(0)
            if c == ']':
                while stack[-1] != '[':
                    res += stack.pop()
                stack.pop()
                while stack != [] and '0' <= stack[-1] <= '9':
                    multiple += stack.pop()
                multiple = int(multiple[::-1])
                cur = list(multiple * res[::-1])
                res = ""
                multiple = ""
                while cur:
                    stack.append(cur.pop(0))
            else:
                stack.append(c)
        return "".join(stack)

if __name__ == '__main__':
    solution = Solution()
    res = solution.decodeString('10[leetcode]')
    print(res)