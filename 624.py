from typing import List
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minimum = arrays[0][0]
        maximum = arrays[0][-1]
        res = 0
        for i in range(1, len(arrays)):
            res = max(res, max(abs(arrays[i][0] - maximum), abs(arrays[i][-1] - minimum)))
            minimum = min(minimum, arrays[i][0])
            maximum = max(maximum, arrays[i][-1])
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.maxDistance([[1,5],[3,4]])
    print(res)