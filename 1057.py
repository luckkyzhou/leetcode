from typing import List
from collections import defaultdict
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        hashmap = defaultdict(int)
        for i in range(len(workers)):
            for j in range(len(bikes)):
                distance = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                hashmap[(i, j)] = distance
        sortHashmap = sorted(hashmap.items(), key=lambda x: (x[1], x[0][0], x[0][1]))
        workersUsed = [True for _ in range(len(workers))]
        bikesUsed = [True for _ in range(len(bikes))]
        res = [0 for _ in range(len(workers))]
        for i in range(len(sortHashmap)):
            if workersUsed[sortHashmap[i][0][0]] and bikesUsed[sortHashmap[i][0][1]]:
                res[sortHashmap[i][0][0]] = sortHashmap[i][0][1]
                workersUsed[sortHashmap[i][0][0]] = False
                bikesUsed[sortHashmap[i][0][1]] = False
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.assignBikes([[0,0],[1,1],[2,0]],[[1,0],[2,2],[2,1]])
    print(res)
