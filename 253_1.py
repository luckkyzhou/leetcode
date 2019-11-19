from typing import List
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        queue = []
        count = 1
        intervals.sort()
        heapq.heappush(queue, intervals[0][1])

        for i in range(1, len(intervals)):
            cur = heapq.heappop(queue)
            if intervals[i][0] < cur:
                count += 1
                heapq.heappush(queue, cur)
            heapq.heappush(queue, intervals[i][1])
        return count