from typing import List
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        res = 0
        Sum = sum(calories[:k])
        for i in range(0, len(calories) - k):
            if Sum < lower: res -= 1
            elif Sum > upper: res += 1
            Sum -= calories[i]
            Sum += calories[i + k]
        if Sum < lower: res -= 1
        elif Sum > upper: res += 1
        return res