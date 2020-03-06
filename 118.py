from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            cur = [1] * (i + 1)
            if i >= 2:
                for j in range(1, i):
                    cur[j] = pre[j] + pre[j - 1]
            res.append(cur)
            pre = cur
        return res