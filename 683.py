from typing import List
class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        days = [0] * len(bulbs)
        for day, position in enumerate(bulbs):
            days[position - 1] = day

        res = float('inf')
        left, right = 0, K + 1
        while right < len(days):
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left, right = i, i + K + 1
                    break
            else:
                res = min(res, max(days[left], days[right]))
                left, right = right, right + K + 1

        return res if res < float('inf') else -1