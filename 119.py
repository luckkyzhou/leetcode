from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(1, rowIndex):
            res.insert(0, 0)
            for j in range(i):
                res[j] += res[j + 1]
        return res