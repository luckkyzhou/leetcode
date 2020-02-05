from typing import List
import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        builds = []
        for building in buildings:
            builds.append((building[0], -building[2]))
            builds.append((building[1], building[2]))
        builds.sort()
        
        maxHeap = []
        heapq.heappush(maxHeap, 0)
        res = []
        prevHeight = 0
        for build in builds:
            if build[1] < 0: heapq.heappush(maxHeap, build[1])
            else:
                maxHeap.pop(maxHeap.index(-build[1]))
                heapq.heapify(maxHeap)
            curHeight = -maxHeap[0]
            if curHeight != prevHeight:
                res.append([build[0], curHeight])
                prevHeight = curHeight
        return res
if __name__ == '__main__':
    solution = Solution()
    res = solution.getSkyline([[15,20,10],[19,24,8]])
    print(res)