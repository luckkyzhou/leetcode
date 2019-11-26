import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        queue = []
        num = dict(Counter(S))
        for key, value in num.items():
            if value > (len(S) + 1) / 2: return ""
            queue.append((-value, key))

        res = []
        heapq.heapify(queue)
        while len(queue) >= 2:
            count1, char1 = heapq.heappop(queue)
            count2, char2 = heapq.heappop(queue)
            res.append(char1)
            res.append(char2)
            if count1 + 1 != 0: heapq.heappush(queue, (count1 + 1, char1))
            if count2 + 1 != 0: heapq.heappush(queue, (count2 + 1, char2))

        if queue:
            return "".join(res) + queue[0][1]
        else:
            return "".join(res)