# -*- coding: utf-8 -*-

from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()
        count = 1
        head = []
        heapq.heappush(head, intervals[0][1])

        for i in range(1, len(intervals)):
            cur = heapq.heappop(head)
            if intervals[i][0] < cur:
                heapq.heappush(head, cur)
                count += 1
            heapq.heappush(head, intervals[i][1])

        return count