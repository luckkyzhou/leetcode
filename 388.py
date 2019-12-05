class Solution:
    def lengthLongestPath(self, input: str) -> int:
        input = input.split("\n")
        res = 0
        stack = []

        for s in input:
            count = s.count("\t")
            s = s[count:]

            # 根据目录的规则pop出之前多余的文件夹
            while len(stack) > count:
                stack.pop()

            if "." in s:
                # 当前文件名长度+目录中的/长度
                cur = len(s) + len(stack)
                for dir in stack:
                    cur += len(dir)
                res = max(res, cur)
            else:
                stack.append(s)
        return res