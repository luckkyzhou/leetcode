from typing import List
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        for log in logs:
            logStr = log.split(":")
            if logStr[1] == "start":
                stack.append((int(logStr[0]), int(logStr[2])))
            else:
                cur = stack.pop()
                time = int(logStr[2]) - cur[1] + 1
                res[cur[0]] += time
                if stack:
                    res[stack[-1][0]] -= time
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"])
    print(res)